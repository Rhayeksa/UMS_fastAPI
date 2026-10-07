import json

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
            "link": "/",
        },
        {
            "icon": "<i class='fa-solid fa-users me-2'></i>",
            "text": "Users",
            "link": "#",
        },
        {
            "icon": "<i class='fa-solid fa-screwdriver-wrench me-2'></i>",
            "text": "Tools",
            "sub": [
                {
                    "icon": "<i class='fa-solid fa-file-import me-2'></i>",
                    "text": "Import",
                    "link": "#",
                },
                {
                    "icon": "<i class='fa-solid fa-file-export me-2'></i>",
                    "text": "Export",
                    "link": "#",
                },
            ],
        },
        {
            "icon": "<i class='fa-solid fa-user me-2'></i>",
            "text": "My Profile",
            # "link": f"/profile/{user['user_id']}",
        },
        {
            "icon": "<i class='fa-solid fa-circle-xmark me-2'></i>",
            "text": "Logout",
            "link": "/logout",
        },
    ]
    # if user["role"] == "player":
    #     result = [i for i in result if i["text"] not in ["Leaderboard"]]

    return result
