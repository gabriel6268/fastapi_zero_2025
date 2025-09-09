# Criando teste para verificar o status_code e também a resposta em si

from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero_2025.app import app

client_test = TestClient(app)
router_get = client_test.get('/')


def test_status_code_retorna_200():
    assert router_get.status_code == HTTPStatus.OK


def test_retorna_ola_mundo():
    assert router_get.json() == {'message': 'Olá, Mundo!'}
