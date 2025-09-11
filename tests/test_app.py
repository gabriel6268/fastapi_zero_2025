# Criando teste para verificar o status_code e também a resposta em si

from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero_2025.app import app

client_test = TestClient(app)
get_home = client_test.get('/')
get_inicial = client_test.get('/inicial/')


# testes endpoint /
def test_status_code_retorna_200():
    assert get_home.status_code == HTTPStatus.OK


def test_retorna_ola_mundo():
    assert get_home.json() == {'message': 'Olá, Mundo!'}


# testes endpoint inicial html
def test_inicial_status_code_retorna_200():
    assert get_inicial.status_code == HTTPStatus.OK


def test_inicial_retorna_html_ola_mundo():
    assert (
        get_inicial.text
        == """<html>
        <head>
            <title>
                Olá, mundo
            </title>
        </head>
        <body>
            <h1>Olá, Mundo!!</h1>
        </body>
    </html>"""
    )


# testes endpoint rota criação de usuario
get_create_user = client_test.post(
    '/users/',
    json={
        'id': 1,
        'username': 'Gabriel',
        'email': 'gabriel@example.com',
        'password': '123',
    },
)


def test_create_user_retorna_200():
    assert get_create_user.status_code == HTTPStatus.CREATED


def test_create_user_retorna_dict_infos():
    assert get_create_user.json() == {
        'id': 1,
        'username': 'Gabriel',
        'email': 'gabriel@example.com',
    }
