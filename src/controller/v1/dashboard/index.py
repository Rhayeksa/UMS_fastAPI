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

# from fastapi_timeout import timeout
from src.util.v1.timeout import timeout  # <-- Ganti import ke file buatan sendiri

router = APIRouter()


@router.get(
    path=v1_dashboard,
    response_class=HTMLResponse,
    include_in_schema=False,
)
@limiter.limit("30/minute")  # limit di level API | second, minute, hour, day
@timeout(5.0)
async def f(request: Request):
    # token = request.cookies.get("x-access-token")
    # payload = verify_token(token=token)

    # if not token or isinstance(payload, str):
    #     return RedirectResponse(url="/login")

    try:
        # await asyncio.sleep(6)  # Simulasi proses berat selama 7 detik
        # Saat memanggil log, wajib mengirimkan dictionary 'extra' berisi variabel di atas
        # data_kustom = {"user_id": "Budi99", "ip_address": "192.168.1.5"}
        # logger.info("berhasil", extra=data_kustom)
        data = []
        for i in range(10):
            data.append(
                {
                    "created_at": "2026-12-31 15:30:59",
                    "username": f"Username {i + 1}",
                    "age": 18 + i,
                    "gender": "Pria",
                    "role": "Administrator",
                }
            )
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
                "breadcrumb": [
                    {
                        "icon": "<i class='fa-solid fa-chart-column me-2'></i>",
                        "text": "Dashboard",
                    },
                ],
                "top_10_new_usr": data,
            },
        )
    except Exception as e:  # noqa: BLE001
        return await http_code_500(request, e)
