from fastapi import Request
from slowapi import Limiter
from slowapi.util import get_remote_address

from src.util.v1.verify_token import f as verify_token


def jwt_or_ip_key(request: Request) -> str:
    """
    Priority:
    1. user_id dari JWT
    2. fallback ke IP
    """
    token = request.cookies.get("x-access-token")
    payload = verify_token(token=token)
    if token and not isinstance(payload, str):
        payload = verify_token(token=token)
        return f"user: {payload.get('user_id')}"
    return f"ip: {get_remote_address(request)}"


limiter = Limiter(key_func=jwt_or_ip_key)
