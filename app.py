from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero_2025.schemas import Message, UserDB, UserPublic, UserSchema

app = FastAPI(title='API para estudos', version='1.0')
database = []


# Endpoint inicial para exemplo
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, Mundo!'}


# Endpoint que retorna HTML -> 'Olá, Mundo!'
@app.get('/inicial/', status_code=HTTPStatus.OK, response_class=HTMLResponse)
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
    '/users/',
    status_code=HTTPStatus.CREATED,
    response_model=UserPublic,
)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id
