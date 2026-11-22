# from src.controller.v1.user.add_submit import router as v1_user_add_submit
from src.api.v1.favicon import router as v1_favicon
from src.api.v1.welcome_api import router as v1_welcome_api
from src.controller.v1.auth.login.index import router as v1_login
from src.controller.v1.auth.login.submit import router as v1_login_submit
from src.controller.v1.auth.register.index import router as v1_register

# from src.controller.v1.auth.register.submit import router as v1_register_submit
from src.controller.v1.dashboard.index import router as v1_dashboard

# from src.controller.v1.dashboard.search import router as v1_dashboard_search
from src.controller.v1.log.index import router as v1_log
from src.controller.v1.user.add import router as v1_user_add

# from src.controller.v1.user.edit_submit import router as v1_user_edit_submit
from src.controller.v1.user.delete import router as v1_user_delete
from src.controller.v1.user.detail import router as v1_user_detail
from src.controller.v1.user.edit import router as v1_user_edit
from src.controller.v1.user.export import router as v1_export
from src.controller.v1.user.import_page import router as v1_import_page
from src.controller.v1.user.index import router as v1_user

# from src.controller.v1.log.search import router as v1_log_search
# from src.controller.v1.log.export_excel import router as v1_log_export_excel
# from src.controller.v1.log.export_csv import router as v1_log_export_csv


routers = [
    # === API ===
    v1_favicon,
    v1_welcome_api,
    # === CONTROLLER ===
    v1_dashboard,
    v1_log,
    v1_login,
    v1_login_submit,
    v1_register,
    # v1_register_submit,
    v1_user,
    v1_user_add,
    # v1_user_add_submit,
    v1_user_edit,
    # v1_user_edit_submit,
    v1_user_delete,
    v1_import_page,
    # v1_import_download_template,
    # v1_import_upload,
    v1_export,
    # v1_export_preview,
    # v1_export_excel,
    # v1_export_csv,
    v1_user_detail,
]
