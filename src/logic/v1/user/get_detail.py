from sqlalchemy import text

from src.configs import POSTGRES_SCHEMA, session
from src.util.response import f as response
from src.util.verify_token import f as verify_token


def util_f(user_id: str):
    return session.execute(
        text(
            f"""
                SELECT
                    user_id
                    , created_at
                    , updated_at
                    , username
                    , "password"
                    , "name"
                    , age
                    , gender
                    , "role"
                FROM {POSTGRES_SCHEMA}.tb_users
                WHERE deleted_at IS NULL
                AND user_id = :user_id
                """
        ), {"user_id": user_id}
    ).mappings().fetchone()


async def f(
    user_id: str,
    x_access_token: str = None,
):
    payload = payload_role = None
    try:
        if x_access_token != None:
            payload = verify_token(token=x_access_token)
            if payload == "INVALID_TOKEN":
                return response(code=401, message="Your session is invalid. Please log in again.")
            elif payload == "TOKEN_EXPIRED":
                return response(code=401, message="Your session has expired. Please log in again.")
            query = util_f(user_id=payload.get("user_id"))
            payload_role = query["role"]
            if payload_role and payload_role == "player" and user_id != query["user_id"]:
                return response(code=400, message="You don't have permission to view other players' data.")

        query = util_f(user_id=user_id)
        if not query:
            return response(code=404, message="user not found")
        if payload_role and payload_role == "game_master" and query["role"] == "administrator":
            return response(code=400, message="Game masters are not allowed to view administrators' data.")

        return response(
            code=200,
            data=query,
        )
    except Exception as e:
        print(f"\nError: {e}\n")
    finally:
        session.close()
