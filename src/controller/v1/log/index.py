import json

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse, Response

from src.config import NAV_ICON, NAV_TITLE, templates
from src.urls import v1_log
from src.util.v1.exception_handlers import http_code_500
from src.util.v1.navbar_menu import f as nav_menu
from src.util.v1.rate_limiter import limiter

# from src.v1.util.verify_token import f as verify_token

# from src.v1.util.response import f as response

router = APIRouter()


@router.get(
    path=v1_log,
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
        data = []
        for i in range(50):
            data.append(
                {
                    "log_id": i,
                    "timestamp": "2026-12-31 15:30:59",
                    "username": f"Username {i + 1}",
                    "log": "{'menu': 'users', 'req': 'get'}",
                },
            )
        return templates.TemplateResponse(
            request=request,
            name="page/v1/log/index.html",
            context={
                "navbar": {
                    "title": NAV_TITLE,
                    "icon": NAV_ICON,
                    "menus": await nav_menu(token="token"),
                },
                "auth": {
                    "username": "Administrator",
                    "is_admin": True,
                },
                "breadcrumb": [
                    {"icon": "<i class='fa-solid fa-user-clock me-2'></i>", "text": "Log"},
                ],
                "top_100": data,
            },
        )
    except Exception as e:  # noqa: BLE001
        return await http_code_500(request, e)
