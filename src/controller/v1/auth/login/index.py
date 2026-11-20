import json

from fastapi import APIRouter, Body, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse, Response

from src.config import templates
from src.logic.v1.user.login import f as login
from src.urls import v1_login
from src.util.v1.rate_limiter import limiter
from src.util.v1.response import f as response
from src.util.v1.verify_token import f as verify_token

router = APIRouter()


@router.get(
    path=v1_login,
    response_class=HTMLResponse,
    include_in_schema=False,
)
@limiter.limit("30/minute")  # limit di level API | second, minute, hour, day
async def f(request: Request):
    token = request.cookies.get("x-access-token")
    payload = verify_token(token=token)

    # if token and not isinstance(payload, str):
    #     return RedirectResponse(url="/")

    return templates.TemplateResponse(
        request=request, name="page/v1/user/login.html", context={}
    )
