from http import HTTPStatus
from typing import Any, Dict, Optional

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.util.v1.timezone_now import f as timezone_now


def f(
    code: int,
    message: Optional[str] = None,
    page: Optional[Dict[str, Any]] = None,
    data: Optional[Any] = None,
) -> JSONResponse:
    start_time = timezone_now()
    try:
        http_status = HTTPStatus(code)
        status = http_status.phrase
    except ValueError as e:
        print(f"\nInvalid status code {code}: {e}\n")
        http_status = HTTPStatus.INTERNAL_SERVER_ERROR
        status = http_status.phrase
        # message = str(e) if message is None else message
        message = str(e)
        page = None
        data = None

    result = {
        "datetime": start_time.isoformat(),  # Use ISO 8601 format for datetime
        "status_code": code,
        "status": status,
        "message": message or status,  # If no message, use status as fallback
    }

    if page:
        result["page"] = page
    if data:
        result["data"] = jsonable_encoder(data)
    return JSONResponse(content=result, status_code=http_status)
