from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_should_return_ok_hellor_world():
    client = TestClient(app)  # Arrange

    response = client.get("/")  # Act

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {"message": "Hello world!"}  # assert
