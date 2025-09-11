import pytest
from fastapi.testclient import TestClient

from fastapi_zero_2025.app import app


# Arrange geral para testes
@pytest.fixture
def client():
    return TestClient(app)
