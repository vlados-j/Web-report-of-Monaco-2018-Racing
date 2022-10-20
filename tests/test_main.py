from main import app
import pytest
from flask import url_for


@pytest.fixture()
def client():
    return app.test_client()


def test_index(client):
    with client:
        response = client.get('/')
        assert response.status_code == 302
        assert response.location == url_for('report')


def test_index_wrong_request(client):
    response = client.post('/')
    assert response.status_code == 405


#Вот тут не понимаю из-за чего фейлится тест
@pytest.mark.parametrize("path", ['/report/', '/report/?order=desc'])
def test_report(client, path):
    response = client.get(path)
    assert response.status_code == 200


def test_drivers(client):
    pass


def test_info_for_output():
    pass
