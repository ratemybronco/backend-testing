import pytest
from ratemybronco import create_app


@pytest.fixture
def app():
  app = create_app()
  return app


@pytest.fixture
def client(app):
  return app.test_client()


def test_landing(client):
  assert client.get("/").status_code == 200