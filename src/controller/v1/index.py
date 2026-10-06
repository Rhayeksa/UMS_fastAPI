import json

from fastapi import APIRouter, Body, Request
from fastapi.responses import HTMLResponse, RedirectResponse, Response

from src.config import NAV_ICON, NAV_TITLE, templates
from src.util.v1.exception_handlers import http_code_500
from src.util.v1.navbar_menu import f as nav_menu
from src.util.v1.rate_limiter import limiter

# from src.v1.util.verify_token import f as verify_token

# from src.v1.util.response import f as response

router = APIRouter()


@router.get(
    path="/",
    response_class=HTMLResponse,
    include_in_schema=False,
)
@limiter.limit("30/minute")  # limit di level API | second, minute, hour, day
async def f(request: Request):
    # token = request.cookies.get("x-access-token")
    # payload = verify_token(token=token)

    # if not token or isinstance(payload, str):
    #     return RedirectResponse(url="/login")

    try:
        return templates.TemplateResponse(
            request=request,
            name="page/v1/index.html",
            context={
                "nav_title": NAV_TITLE,
                "nav_icon": NAV_ICON,
                "nav_menu": await nav_menu(token="token"),
                "usr_username": "Administrator",
                "usr_is_administrator": True,
            },
        )
    except Exception as e:
        return await http_code_500(request, e)


# @router.post(
#     path="/",
#     include_in_schema=False,
# )
# @limiter.limit("15/minute")  # limit di level API | second, minute, hour, day
# async def f_post(
#     request: Request,
#     choice: str = Body(..., embed=True),
# ):
#     token = request.cookies.get("x-access-token")
#     payload = verify_token(token=token)

#     if not token or isinstance(payload, str):
#         #     return RedirectResponse(url="/login")
#         # res = Response(status_code=204)
#         # res.headers["HX-Redirect"] = "/login"
#         res = response(code=200)
#         res.headers["HX-Redirect"] = "/login"
#         return res

#     try:
#         data = await play(choice=choice, x_access_token=token)
#         data = json.loads(data.body)
#         return response(
#             code=data["status_code"],
#             message=data["message"],
#             data=data["data"] if data["status_code"] == 200 else None,
#         )
#     except Exception as e:
#         return await http_code_500(request, e)
