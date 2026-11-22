import asyncio
from functools import wraps

from fastapi import HTTPException


def timeout(seconds: float):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await asyncio.wait_for(func(*args, **kwargs), timeout=seconds)
            except TimeoutError:
                raise HTTPException(status_code=504, detail="Request Timeout")

        return wrapper

    return decorator
