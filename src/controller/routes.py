# from src.controller.battle.battle_info_by_user_id import (
#     router as battle_info_by_user_id,
# )
# from src.controller.user.profile import router as profile
from src.controller.v1.index import router as index

# from src.controller.user.login import router as login
# from src.controller.user.logout import router as logout
# from src.controller.user.register import router as register

routes = [
    # page
    index,
    # login,
    # register,
    # profile,
    # battle_info_by_user_id,
    # util
    # logout,
]
