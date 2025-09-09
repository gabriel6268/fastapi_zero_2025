from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


# Endpoint inicial para exemplo
@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Olá, Mundo!'}


# Endpoint para exemplo de html
@app.get('/hello/', response_class=HTMLResponse, status_code=HTTPStatus.OK)
def hello():
    return """
        <html>
            <head>
                <title>Hello, World!</title>
            </head>
            <body>
                <h1>Hello, World!!!</h1>
            </body>
        </html>
    """
