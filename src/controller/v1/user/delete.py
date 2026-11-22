from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from src.config import NAV_ICON, NAV_TITLE, templates
from src.urls import v1_user, v1_user_delete
from src.util.v1.exception_handlers import http_code_500
from src.util.v1.navbar_menu import f as nav_menu
from src.util.v1.rate_limiter import limiter

router = APIRouter()


@router.get(
    path=v1_user_delete + "/{user_id}",
    # response_class=HTMLResponse,
    include_in_schema=False,
)
@limiter.limit("30/minute")  # limit di level API | second, minute, hour, day
async def f(request: Request):
    # token = request.cookies.get("x-access-token")
    # payload = verify_token(token=token)

    # if not token or isinstance(payload, str):
    #     return RedirectResponse(url="/login")
    try:
        return RedirectResponse(url=v1_user)
    except Exception as e:  # noqa: BLE001
        return await http_code_500(request, e)
