from fastapi import APIRouter
from fastapi.responses import FileResponse

from src.config import DIR_STATIC
from src.urls import favicon

router = APIRouter()


@router.get(
    include_in_schema=False,
    path=f"{favicon}",
)
async def f():
    return FileResponse(f"{DIR_STATIC}/favicon/favicon.ico")
