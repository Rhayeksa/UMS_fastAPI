import uuid

from sqlalchemy import text

from src.config import POSTGRES_SCHEMA, session
from src.util.v1.password import hash_password
from src.util.v1.response import f as response
from src.util.v1.timezone_now import f as timezone_now


async def f(
    name: str,
    username: str,
    password: str,
    age: int = None,
    gender: str = None,
    role: str = "player",
):
    try:
        if age and not (age >= 1 and age <= 250):
            return response(code=400, message="Age must be between 1 and 250.")
        if gender and gender.upper() not in ("M", "F"):
            return response(code=400, message="Gender must be either 'M' or 'F'.")
        if role not in ("administrator", "player"):
            return response(
                code=400, message="Role must be either 'administrator' or 'player'."
            )

        data = (
            session.execute(
                text(
                    f"""
                SELECT count(1)
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
        if data["count"]:
            return response(code=400, message="username already exists")

        user_id = uuid.uuid4()
        now = timezone_now()
        session.execute(
            text(
                f"""
                INSERT INTO {POSTGRES_SCHEMA}.tb_users(
                    user_id
                    , created_at
                    , updated_at
                    , username
                    , "password"
                    , "name"
                    , age
                    , gender
                    , role
                ) VALUES(
                    :user_id
                    , :created_at
                    , :updated_at
                    , :username
                    , :password
                    , :name
                    , :age
                    , :gender
                    , :role
                )
                """
            ),
            {
                "user_id": user_id,
                "created_at": now,
                "updated_at": now,
                "username": username,
                "password": hash_password(password),
                "name": name,
                "age": age,
                "gender": gender,
                "role": role,
            },
        )

        session.commit()
        return response(code=201)
    except Exception as e:
        session.rollback()
        print(f"\nError : {e}\n")
        return response(code=500)
    finally:
        session.close()
