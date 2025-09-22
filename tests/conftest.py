from contextlib import contextmanager
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session

from fastapi_zero_2025.app import app
from fastapi_zero_2025.models import User, table_registry


# Arrange geral para testes
@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    # criando conexão com o banco de dados
    engine = create_engine('sqlite:///:memory:')

    # dentro da conexão criamos a tabela
    table_registry.metadata.create_all(engine)

    # abrindo sessao de troca entre o codigo e o banco de dados
    with Session(engine) as session:
        yield session

    # deletando s tabela
    table_registry.metadata.drop_all(engine)


@contextmanager
def mock_db_time_context(model=User, time=datetime(2025, 5, 20)):
    def fake_time_hook(mapper, connection, target):
        event.listen(model, 'before_insert', fake_time_hook)

        yield time

        event.remove(model, 'before_insert', fake_time_hook)


@pytest.fixture
def mock_db_time():
    return mock_db_time_context()
