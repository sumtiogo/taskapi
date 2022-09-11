from flask import Flask
from flask.testing import FlaskClient

from taskapi.db import get_db


def test_get(client: FlaskClient):
    # act
    response = client.get('/tasks')
    # assertion
    assert response.status_code == 200
    assert response.json == {'result': []}


def test_get_given_data(app: Flask, client: FlaskClient):
    # arrange
    with app.app_context():
        get_db().executescript('''
        INSERT INTO task (status)
        VALUES (true), (false)
        ''')
    # act
    response = client.get('/tasks')
    # assertion
    assert response.status_code == 200
    # TODO: here is over-specification, result no need to keep order,
    # find a better assertion tool to compare two arrays
    assert response.json == {'result': [
        {'id': 1, 'status': True},
        {'id': 2, 'status': False},
    ]}
