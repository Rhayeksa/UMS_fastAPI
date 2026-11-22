from fastapi import Request
from slowapi.errors import RateLimitExceeded

from src.config import logger, templates
from src.util.v1.navbar_menu import f as navbar_menu
from src.util.v1.response import f as response


async def http_code_429(request: Request, exc: RateLimitExceeded):
    print(f"\nError {exc}\n")
    accept = request.headers.get("accept", "")
    if "text/html" in accept:
        token = request.cookies.get("x-access-token")
        return templates.TemplateResponse(
            request=request,
            name="page/v1/error.html",
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
    logger.exception("\nError 500 | Internal Server Error")
    return templates.TemplateResponse(
        request=request,
        name="page/v1/error.html",
        context={
            "err": {"code": 500, "msg": "Internal Server Error"},
        },
        status_code=500,
    )


async def http_code_404(request: Request, _exc: Exception):
    print(f"\nError {_exc}\n")
    return templates.TemplateResponse(
        request=request,
        name="page/v1/error.html",
        context={
            "err": {"code": 404, "msg": "Page Not Found"},
        },
        status_code=404,
    )


async def http_code_504(request: Request, _exc: Exception):
    return templates.TemplateResponse(
        request=request,
        name="page/v1/error.html",
        context={"err": {"code": 504, "msg": "Request Timeout / Gateway Timeout"}},
        status_code=504,
    )
