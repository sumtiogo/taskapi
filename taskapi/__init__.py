import os

from flask import Flask, request

from taskapi.db import get_db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'taskapi.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    from . import db
    db.init_app(app)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/tasks')
    def get_tasks():
        db = get_db()
        records = db.execute('''
        SELECT id, name, status from task
        ''').fetchall()
        return {'result': records}, 200

    @app.route('/task', methods=('POST',))
    def create_task():
        name = request.form['name']
        db = get_db()
        cursor = db.execute('''
        INSERT INTO task (name, status)
        VALUES (?, ?)
        RETURNING id, name, status
        ''', (name, False))
        data = cursor.fetchone()
        db.commit()
        return {'result': data}, 201

    return app
