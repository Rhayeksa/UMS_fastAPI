from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from src.configs import templates
from src.util.rate_limiter import limiter
from src.util.verify_token import f as verify_token

router = APIRouter()


@router.get(
    path="/register",
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
        name="pages/user/register.html",
        context={"request": request}
    )
