from sqlalchemy import select  # type: ignore

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username="annicchino",
        email="annicchino@email.com",
        password="my-p@ssword",
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == "annicchino@email.com")
    )

    assert result.username == "annicchino"
