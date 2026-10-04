import json

from fastapi import APIRouter

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


@router.get(
    path="/api",
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
    },
)
async def f():
    try:
        return response(code=200, message=res_200["message"])
    except Exception as e:
        print(f"\nError : {e}\n")
        return response(code=res_500["code"])
