import json

from fastapi import Body, Request

from src.config import router
from src.logic.v1.dashboard.get_data import f as get_data
from src.util.v1.exception_handlers import http_code_500
from src.util.v1.rate_limiter import limiter

# from src.v1.util.verify_token import f as verify_token
from src.util.v1.response import f as response


@router.post(
    path="/",
    include_in_schema=False,
)
@limiter.limit("5/minute")  # limit di level API | second, minute, hour, day
async def f_post(
    request: Request,
    choice: str = Body(..., embed=True),
):
    # token = request.cookies.get("x-access-token")
    # payload = verify_token(token=token)

    # if not token or isinstance(payload, str):
    #     #     return RedirectResponse(url="/login")
    #     # res = Response(status_code=204)
    #     # res.headers["HX-Redirect"] = "/login"
    #     res = response(code=200)
    #     res.headers["HX-Redirect"] = "/login"
    #     return res

    try:
        data = await get_data(...)
        data = json.loads(data.body)
        return response(
            code=data["status_code"],
            message=data["message"],
            data=data["data"] if data["status_code"] == 200 else None,
        )
    except Exception as e:
        return await http_code_500(request, e)
