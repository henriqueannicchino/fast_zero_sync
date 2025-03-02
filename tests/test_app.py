from http import HTTPStatus


def test_read_root_should_return_ok_hellor_world(client):
    response = client.get("/")  # Act

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {"message": "Hello world!"}  # assert


def test_create_user(client):
    response = client.post(  # UserSchema
        "/users/",
        json={
            "username": "testusername",
            "password": "password",
            "email": "test@test.com",
        },
    )

    # Returned the right code status?
    assert response.status_code == HTTPStatus.CREATED

    # Validate UserPublic
    assert response.json() == {
        "username": "testusername",
        "email": "test@test.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "testusername",
                "email": "test@test.com",
                "id": 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "password": "123",
            "username": "testusername2",
            "email": "test@test.com",
            "id": 1,
        },
    )
    assert response.json() == {
        "username": "testusername2",
        "email": "test@test.com",
        "id": 1,
    }


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "User deleted"}
