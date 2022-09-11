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
        INSERT INTO task (name, status)
        VALUES ('cook', true), ('laundry', false)
        ''')
    # act
    response = client.get('/tasks')
    # assertion
    assert response.status_code == 200
    # TODO: here is over-specification, result no need to keep order,
    # find a better assertion tool to compare two arrays
    assert response.json == {'result': [
        {'id': 1, 'name': 'cook', 'status': True},
        {'id': 2, 'name': 'laundry', 'status': False},
    ]}


def test_post(client: FlaskClient):
    response = client.post('/task', data={'name': '買晚餐'})
    assert response.json == {'result': {'name': '買晚餐', 'status': 0, 'id': 1}}


def test_put(app: Flask, client: FlaskClient):
    # arrange
    with app.app_context():
        get_db().executescript('''
        INSERT INTO task (name, status)
        VALUES ('睡覺', false)
        ''')
    # action
    response = client.put('/task/1', data={
        'name': '買早餐',
        'status': 1,
        'id': 1
    })
    # assertion
    assert response.json == {'result': {
        "name": "買早餐",
        "status": 1,
        "id": 1
    }}


def test_delete(app: Flask, client: FlaskClient):
    # arrange
    with app.app_context():
        get_db().executescript('''
        INSERT INTO task (name, status)
        VALUES ('睡覺', false)
        ''')
    # action
    response = client.delete('/task/1')
    # assertion
    assert response.status_code == 200
    tasks = client.get('/tasks').json['result']
    assert tasks == []
