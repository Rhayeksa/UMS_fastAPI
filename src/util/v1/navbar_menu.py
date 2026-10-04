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
    result = [
        {
            "icon": "<i class='fa-solid fa-play me-2'></i>",
            "text": "Let's Play",
            "link": "/",
        },
        {
            "icon": "<i class='fa-solid fa-rectangle-list me-2'></i>",
            "text": "Battle Information",
            # "link": f"/battle/user/{user['user_id']}",
        },
        {
            "icon": "<i class='fa-solid fa-ranking-star me-2'></i>",
            "text": "Leaderboard",
            "link": "#",
        },
        {
            "icon": "<i class='fa-solid fa-user me-2'></i>",
            "text": "Profile",
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
