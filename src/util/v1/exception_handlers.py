from fastapi import Request
from slowapi.errors import RateLimitExceeded

from src.config import templates
from src.util.v1.navbar_menu import f as navbar_menu
from src.util.v1.response import f as response


async def http_code_429(request: Request, exc: RateLimitExceeded):
    print(f"\nError {exc}\n")
    accept = request.headers.get("accept", "")
    if "text/html" in accept:
        token = request.cookies.get("x-access-token")
        return templates.TemplateResponse(
            request=request,
            name="v1/page/error.html",
            context={
                "request": request,
                "token": token,
                "err": {"code": 429, "msg": "Too Many Requests"},
                "navbar_menu": await navbar_menu(token=token),
            },
            status_code=429,
        )
    return response(code=429, message="Too many requests, please try again later.")


async def http_code_500(request: Request, exc: Exception):
    print(f"\nError 500: {exc}\n")
    return templates.TemplateResponse(
        request=request,
        name="v1/page/error.html",
        context={
            "request": request,
            "err": {"code": 500, "msg": "Internal Server Error"},
        },
        status_code=500,
    )


async def http_code_404(request: Request, exc: Exception = None):
    print(f"\nError {exc}\n")
    return templates.TemplateResponse(
        request=request,
        name="v1/page/error.html",
        context={
            "request": request,
            "err": {"code": 404, "msg": "Page Not Found"},
        },
        status_code=404,
    )
