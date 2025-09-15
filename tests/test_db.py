# teste para modelo do banco de dados
from dataclass import asdict
from sqlalchemy import select

from fastapi_zero_2025.models import User


def test_create_user_db(session, mock_db_time):

    with mock_db_time(model=User) as time:
        new_user = User(
            username='test', email='test@test.com.br', password='test123'
        )

        session.add(new_user)
        session.commit()

        user = session.scalar(select(User).where(User.username == 'test'))

    assert asdict(user) == {
        'id': 1,
        'username': 'test',
        'email': 'test@test.com.br',
        'password': 'test123'
        'create_at': time,
    }
