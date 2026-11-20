from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get(
    path="/logout",
    include_in_schema=False,
)
async def f():
    res = RedirectResponse(url="/login")
    res.delete_cookie(key="x-access-token", path="/")
    return res
