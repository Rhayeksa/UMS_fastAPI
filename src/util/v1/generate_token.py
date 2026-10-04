from datetime import timedelta

import jwt

from src.config import JWT_ACCESS_TOKEN_EXPIRE_HOURS, JWT_ALGORITHM, JWT_SECRET_KEY
from src.util.v1.timezone_now import f as timezone_now


def f(payload: dict) -> dict:
    # print(
    #     f">>> timedelta: {timedelta(hours=float(JWT_ACCESS_TOKEN_EXPIRE_HOURS))}")
    # print(
    #     f">>> timezone_now: {timezone_now(default=True)}")
    expires_at = timezone_now(default=True) + timedelta(
        hours=float(JWT_ACCESS_TOKEN_EXPIRE_HOURS)
    )
    # print(
    #     f">>> expires_at: {expires_at}")
    payload["exp"] = int(expires_at.timestamp())
    payload["iat"] = int(timezone_now(default=True).timestamp())
    return {
        "x-access-token": jwt.encode(
            payload=payload, key=JWT_SECRET_KEY, algorithm=JWT_ALGORITHM
        )
    }
