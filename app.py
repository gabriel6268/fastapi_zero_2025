from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from fastapi_zero_2025.schemas import (
    Message,
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI(title='API para estudos', version='1.0')
database = []
tag_get = 'Leitura de usuário'
tag_post = 'Criação de usuário'
tag_put = 'Atualização de usuário'
tag_delete = 'Remoção de usuário'


# Endpoint inicial para exemplo
@app.get(
    '/', status_code=HTTPStatus.OK, response_model=Message, tags=[tag_get]
)
def read_root():
    return {'message': 'Olá, Mundo!'}


# Endpoint que retorna HTML -> 'Olá, Mundo!'
@app.get(
    '/inicial/',
    status_code=HTTPStatus.OK,
    response_class=HTMLResponse,
    tags=[tag_get],
)
def ola_mundo():
    return """<html>
        <head>
            <title>
                Olá, mundo
            </title>
        </head>
        <body>
            <h1>Olá, Mundo!!</h1>
        </body>
    </html>"""


# Endpoint para criação de usuario
@app.post(
    '/create_user/',
    status_code=HTTPStatus.CREATED,
    response_model=UserPublic,
    tags=[tag_post],
)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


# Endpoint para recuperar todos os usuarios
@app.get(
    '/users/',
    response_model=UserList,
    status_code=HTTPStatus.OK,
    tags=[tag_get],
)
def read_users():
    return {'users': database}


@app.get(
    '/user/{user_id}/',
    response_model=UserPublic,
    status_code=HTTPStatus.OK,
    tags=[tag_get],
)
def read_user_id(user_id: int):
    if user_id < 0 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    return database[user_id - 1]


# Endpoint para alteração dos usuarios por id
@app.put(
    '/users/{user_id}/',
    status_code=HTTPStatus.OK,
    response_model=UserPublic,
    tags=[tag_put],
)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id
    return user_with_id


# Endpoint para exclusão de usuario por id
@app.delete(
    '/users/delete/{user_id}/', tags=[tag_delete], response_model=UserPublic
)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    user_del = database.pop(user_id - 1)
    return user_del
