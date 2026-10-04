import json

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from src.api.v1.user.util.get_detail import f as get_detail
from src.configs import templates
from src.util.exception_handlers import http_code_404, http_code_500
from src.util.navbar_menu import f as navbar_menu
from src.util.rate_limiter import limiter
from src.util.verify_token import f as verify_token

router = APIRouter()


@router.get(
    path="/profile/{user_id}",
    response_class=HTMLResponse,
    include_in_schema=False,
)
@limiter.limit("5/minute")  # limit di level API | second, minute, hour, day
async def f(request: Request, user_id: str):
    token = request.cookies.get("x-access-token")
    payload = verify_token(token=token)

    if not token or isinstance(payload, str):
        return RedirectResponse(url="/login")

    try:
        user = await get_detail(user_id=user_id, x_access_token=token)
        user = json.loads(user.body)
        if user["status_code"] == 400:
            print(f"user profile: {user}")
            return await http_code_404(request)

        user = user["data"]
        return templates.TemplateResponse(
            name="pages/user/profile.html",
            context={
                "request": request,
                "game_master_icon": True if user["role"] in ["administrator", "game_master"] else False,
                "navbar_menu": await navbar_menu(token=token),
                "user": {
                    "user_id": user["user_id"],
                    "name": user["name"],
                    "age": user["age"],
                    "gender": user["gender"],
                    "username": user["username"],
                    # "password": user["password"],
                },
            }
        )
    except Exception as e:
        return await http_code_500(request, e)
