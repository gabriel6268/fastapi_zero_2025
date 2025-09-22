from http import HTTPStatus

from fastapi import HTTPException


def validate(user_id: int, database: list):
    if user_id < 0 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    else:
        pass
