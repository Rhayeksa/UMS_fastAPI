import json

from fastapi import APIRouter, Body, Request
from fastapi.responses import HTMLResponse, RedirectResponse, Response

from src.config import NAV_ICON, NAV_TITLE, logger, templates
from src.urls import v1_dashboard

# from src.v1.util.verify_token import f as verify_token
# from src.v1.util.response import f as response
from src.util.v1.exception_handlers import http_code_500
from src.util.v1.navbar_menu import f as nav_menu
from src.util.v1.rate_limiter import limiter

router = APIRouter()


@router.get(
    path=v1_dashboard,
    # path="/",
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
        # Saat memanggil log, wajib mengirimkan dictionary 'extra' berisi variabel di atas
        # data_kustom = {"user_id": "Budi99", "ip_address": "192.168.1.5"}
        # logger.info("berhasil", extra=data_kustom)

        return templates.TemplateResponse(
            request=request,
            name="page/v1/index.html",
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
                "top_10_new_usr": [
                    {
                        "created_at": "2026-12-31 15:30:59",
                        "username": "Rhayeksa",
                        "role": "Administrator",
                        "gender": "Male",
                        "age": "28",
                    },
                    {
                        "created_at": "2026-12-31 15:30:59",
                        "username": "Rhayeksa",
                        "role": "Administrator",
                        "gender": "Male",
                        "age": "28",
                    },
                    {
                        "created_at": "2026-12-31 15:30:59",
                        "username": "Rhayeksa",
                        "role": "Administrator",
                        "gender": "Male",
                        "age": "28",
                    },
                    {
                        "created_at": "2026-12-31 15:30:59",
                        "username": "Rhayeksa",
                        "role": "Administrator",
                        "gender": "Male",
                        "age": "28",
                    },
                    {
                        "created_at": "2026-12-31 15:30:59",
                        "username": "Rhayeksa",
                        "role": "Administrator",
                        "gender": "Male",
                        "age": "28",
                    },
                ],
            },
        )
    except Exception as e:  # noqa: BLE001
        return await http_code_500(request, e)
