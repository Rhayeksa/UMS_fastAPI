# import asyncio
import json

from fastapi import APIRouter
from fastapi_timeout import timeout

from src.config import logger
from src.urls import api
from src.util.v1.response import f as response

router = APIRouter()
res_200 = response(code=200, message="Welcome to API UMS")
res_200 = json.loads(res_200.body)
res_200 = {
    "code": res_200["status_code"],
    "message": res_200["message"],
    "res": res_200,
}
res_500 = response(code=500)
res_500 = json.loads(res_500.body)
res_500 = {
    "code": res_500["status_code"],
    "res": res_500,
}
res_504 = {
    "detail": "Request processing time exceeded limit",
    "timeout_seconds": 1,
    "processing_time": 1.001,
}


@router.get(
    path=f"{api}",
    name="Welcome API",
    summary="Welcome API",
    responses={
        200: {
            "description": "Welcome API",
            "content": {"application/json": {"example": res_200["res"]}},
        },
        500: {
            "description": "Internal server error",
            "content": {"application/json": {"example": res_500["res"]}},
        },
        504: {
            "description": "Gateway Timeout",
            "content": {"application/json": {"example": res_504}},
        },
    },
)
@timeout(1.0)
async def f():
    try:
        # x = 3 / 0
        # await asyncio.sleep(6)  # Simulasi proses berat selama 7 detik
        return response(code=200, message=res_200["message"])
    except Exception:  # noqa: BLE001
        logger.exception("\nError 500 | Internal Server Error")
        return response(code=res_500["code"])
