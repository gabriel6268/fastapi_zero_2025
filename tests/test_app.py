# Criando teste para verificar o status_code e também a resposta em si

from http import HTTPStatus


# testes endpoint home
def test_status_code_retorna_200(client):
    get_home = client.get('/')
    assert get_home.status_code == HTTPStatus.OK


def test_retorna_ola_mundo(client):
    get_home = client.get('/')
    assert get_home.json() == {'message': 'Olá, Mundo!'}


# testes endpoint inicial html
def test_inicial_status_code_retorna_200(client):
    get_inicial = client.get('/inicial/')
    assert get_inicial.status_code == HTTPStatus.OK


def test_inicial_retorna_html_ola_mundo(client):
    get_inicial = client.get('/inicial/')
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
def test_create_user_retorna_dict_infos(client):
    response = client.post(
        '/create_user/',
        json={
            'id': 1,
            'username': 'Gabriel',
            'email': 'gabriel@example.com',
            'password': '123',
        },
    )

    assert response.json() == {
        'id': 1,
        'username': 'Gabriel',
        'email': 'gabriel@example.com',
    }
    assert response.status_code == HTTPStatus.CREATED


# teste endpoint leitura todos os usuarios
def test_read_users_retorna_dict_infos(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {'username': 'Gabriel', 'email': 'gabriel@example.com', 'id': 1}
        ]
    }


# teste endpoint leitura usuario por id
def test_read_user_id_retorna_dict_info(client):
    response = client.get('/user/1/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Gabriel',
        'email': 'gabriel@example.com',
        'id': 1,
    }


def test_read_user_id_not_found(client):
    response = client.get('/user/10/')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


# teste endpoint atualização usuario por id
def test_update_user_retorna_user_att(client):
    response = client.put(
        '/users/1/',
        json={
            'id': 1,
            'username': 'Ana',
            'email': 'ana@example.com',
            'password': '123',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'Ana',
        'email': 'ana@example.com',
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/2/',
        json={
            'id': 1,
            'username': 'Ana',
            'email': 'ana@example.com',
            'password': '123',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


# teste endpoint delecao de usuario por id
def test_delete_user(client):
    response = client.delete('/users/delete/1/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'Ana',
        'email': 'ana@example.com',
    }


def test_delete_user_not_found(client):
    response = client.delete('/users/delete/10/')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
