import json

from fastapi import APIRouter, Body, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse, Response
from src.api.v1.user.util.login import f as login

from src.config import templates
from src.util.v1.rate_limiter import limiter
from src.util.v1.response import f as response
from src.util.v1.verify_token import f as verify_token

router = APIRouter()


@router.get(
    path="/login",
    response_class=HTMLResponse,
    include_in_schema=False,
)
@limiter.limit("30/minute")  # limit di level API | second, minute, hour, day
async def f(request: Request):
    token = request.cookies.get("x-access-token")
    payload = verify_token(token=token)

    if token and not isinstance(payload, str):
        return RedirectResponse(url="/")

    return templates.TemplateResponse(
        name="pages/user/login.html", context={"request": request}
    )


@router.post(
    path="/login",
    include_in_schema=False,
)
@limiter.limit("5/minute")  # limit di level API | second, minute, hour, day
async def f_post(
    request: Request,
    username: str = Body(...),
    password: str = Body(...),
):
    token = await login(username=username, password=password)
    # code = 200
    # msg = None

    if token.status_code != 200:
        code = token.status_code
        token = json.loads(token.body)
        msg = token["message"]
        # return JSONResponse(content={"msg": msg}, status_code=code)
        return response(code=code, message=msg)

    token = json.loads(token.body)
    # msg = token["message"]
    # res = JSONResponse(content={"msg": msg}, status_code=code)
    # res = Response(status_code=204)
    res = response(code=200)
    res.headers["HX-Redirect"] = "/"
    res.set_cookie("x-access-token", token["data"]["x-access-token"])
    return res
