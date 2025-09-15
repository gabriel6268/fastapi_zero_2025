# teste para modelo do banco de dados
from sqlalchemy import select

from fastapi_zero_2025.models import User


def test_create_user_db(session):
    new_user = User(
        username='test', email='test@test.com.br', password='test123'
    )

    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'test'))

    assert user.password == 'test123'
