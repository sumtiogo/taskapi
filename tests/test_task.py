from flask.testing import FlaskClient


def test_get(client: FlaskClient):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert response.json == {'result': []}
