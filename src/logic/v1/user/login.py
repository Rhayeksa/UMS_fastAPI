from sqlalchemy import text

from src.config import POSTGRES_SCHEMA, session
from src.util.v1.generate_token import f as generate_token
from src.util.v1.password import verify_password
from src.util.v1.response import f as response


async def f(
    username: str,
    password: str,
):
    try:
        query = (
            session.execute(
                text(
                    f"""
                SELECT user_id, username, password, role
                FROM {POSTGRES_SCHEMA}.tb_users
                WHERE deleted_at IS NULL
                AND username = :username
                """
                ),
                {"username": username},
            )
            .mappings()
            .fetchone()
        )
        if not query or not verify_password(plain=password, hashed=query["password"]):
            return response(code=400, message="Invalid username or password")

        session.commit()
        return response(
            code=200, data=generate_token(payload={"user_id": query["user_id"]})
        )
    except Exception as e:
        session.rollback()
        print(f"\nError : {e}\n")
        return response(code=500)
    finally:
        session.close()
