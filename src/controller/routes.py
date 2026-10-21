# from src.controller.v1.dashboard.filter import router as v1_dashboard_filter
from src.controller.v1.dashboard.index import router as v1_dashboard_index
from src.controller.v1.log.index import router as log
from src.controller.v1.user.login import router as login
from src.controller.v1.user.register import router as register

# from src.controller.v1.user.logout import router as logout

routes = [
    v1_dashboard_index,
    login,
    register,
    log,

    # profile,
    # logout,
]
