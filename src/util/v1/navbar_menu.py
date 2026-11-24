import json

from src.urls import (
    v1_dashboard,
    v1_log,
    v1_logout,
    v1_user,
    v1_user_add,
    v1_user_export,
    v1_user_import,
)

# from src.v1.api.user.util.get_detail import f as get_detail
from src.util.v1.verify_token import f as verify_token


async def f(token: str):
    # payload = verify_token(token=token)
    # if isinstance(payload, str):
    #     return []
    # user = payload["user_id"]
    # user = await get_detail(user_id=user)
    # user = json.loads(user.body)
    # user = user["data"]
    # <i class="fa-solid fa-users"></i>
    result = [
        {
            "icon": "<i class='fa-solid fa-chart-column me-2'></i>",
            "text": "Dashboard",
            "link": v1_dashboard,
        },
        {
            "icon": "<i class='fa-solid fa-users me-2'></i>",
            "text": "User",
            "sub": [
                {
                    "icon": "<i class='fa-solid fa-users me-2'></i>",
                    "text": "Users",
                    "link": v1_user,
                },
                {
                    "icon": "<i class='fa-solid fa-user-plus me-2'></i>",
                    "text": "Add",
                    "link": v1_user_add,
                },
                {
                    "icon": "<i class='fa-solid fa-file-import me-2'></i>",
                    "text": "Import",
                    "link": v1_user_import,
                },
                {
                    "icon": "<i class='fa-solid fa-file-export me-2'></i>",
                    "text": "Export",
                    "link": v1_user_export,
                },
            ],
        },
        {
            "icon": "<i class='fa-solid fa-user-clock me-2'></i>",
            "text": "Log",
            "link": v1_log,
        },
        {
            "icon": "<i class='fa-solid fa-user me-2'></i>",
            "text": "My Profile",
            # "link": f"{v1_user}/{user['user_id']}",
            "link": f"{v1_user}/f47ac10b-58cc-4372-a567-0e02b2c3d479",
        },
        {
            "icon": "<i class='fa-solid fa-circle-xmark me-2'></i>",
            "text": "Logout",
            "link": v1_logout,
        },
    ]
    # if user["role"] == "player":
    #     result = [i for i in result if i["text"] not in ["Leaderboard"]]

    return result
