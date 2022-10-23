import application_vlados
from main import app
from application import *
import pytest
from flask import url_for
from application_vlados import *
from datetime import datetime
from unittest.mock import patch, Mock, mock_open


@pytest.fixture()
def client():
    from main import app
    app.config['TESTING'] = True
    return app.test_client()


def test_index(client):
    with client:
        response = client.get('/')
        assert response.status_code == 302
        assert response.location == url_for('report_f1.report')


def test_index_wrong_request(client):
    response = client.post('/')
    assert response.status_code == 405


# def test_of_test():
#     print(processing_data('../application/files/start.log', '../application/files/end.log',
#                           '../application/files/abbreviations.txt'))

#Вот в этой функции нужна помощь
@pytest.mark.parametrize("path", ['/report/', '/report/?order=desc'])
@patch('application_vlados.processing_data')
def test_report(mock_processing_data, client, path):
    mock_processing_data.return_value = {'Sebastian Vettel':
                                             Racer('Sebastian Vettel', 'SVF', 'FERRARI',
                                                   datetime(2018, 5, 24, 12, 2, 58, 917),
                                                   datetime(2018, 5, 24, 12, 4, 3, 332)),
                                         'Daniel Ricciardo':
                                             Racer('Daniel Ricciardo', 'DRR', 'RED BULL RACING TAG HEUER', None, None)}
    response = client.get(path)
    print(response.status_code)
    assert response.status_code == 200


@pytest.mark.parametrize("path", ['/report/drivers/', '/report/drivers/?abbreviation=SVF'])
def test_drivers(client, path):
    response = client.get(path, content_type='html/text')
    assert response.status_code == 200, response.content


def test_info_for_output():
    racer1 = Racer('Sebastian Vettel', 'SVF', 'FERRARI', datetime(2018, 5, 24, 12, 2, 58, 917000),
                   datetime(2018, 5, 24, 12, 4, 3, 332))
    racer2 = Racer('Esteban Ocon', 'EOF', 'FORCE INDIA MERCEDES', datetime(2018, 5, 24, 12, 17, 58, 810),
                   datetime(2018, 5, 24, 12, 12, 11, 838))
    structured_data = {racer1.name: racer1, racer2.name: racer2}
    info_for_output(structured_data, 'desc')
    assert racer1.place == 1
    assert racer2.place == '-'
