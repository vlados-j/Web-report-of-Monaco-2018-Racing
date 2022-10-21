from main import app, info_for_output
import pytest
from flask import url_for
from application_vlados import Racer, processing_data
from datetime import datetime


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


@pytest.mark.parametrize("path", ['/report/', '/report/?order=desc'])
def test_report(client, path):
    response = client.get(path, content_type='html/text')
    assert response.status_code == 200


@pytest.mark.parametrize("path", ['/report/drivers/', '/report/drivers/?abbreviation=SVF'])
def test_drivers(client, path):
    response = client.get(path, content_type='html/text')
    assert response.status_code == 200


def test_info_for_output():
    racer1 = Racer('Sebastian Vettel', 'SVF', 'FERRARI', datetime(2018, 5, 24, 12, 2, 58, 917000),
                   datetime(2018, 5, 24, 12, 4, 3, 332))
    racer2 = Racer('Esteban Ocon', 'EOF', 'FORCE INDIA MERCEDES', datetime(2018, 5, 24, 12, 17, 58, 810),
                   datetime(2018, 5, 24, 12, 12, 11, 838))
    structured_data = {racer1.name: racer1, racer2.name: racer2}
    info_for_output(structured_data, 'desc')
    assert racer1.place == 1
    assert racer2.place == '-'
