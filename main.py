from fastapi import FastAPI

# from src.configs import DIR_STATIC
# from src.controller.routes import routes as routes_controller
# from src.util.exception_handlers import http_code_404, http_code_429, http_code_500
# from src.util.rate_limiter import limiter
from starlette.middleware.cors import CORSMiddleware

# from fastapi.staticfiles import StaticFiles
# from slowapi.errors import RateLimitExceeded
from src.v1.api.routes import routes as routes_api

# === CONFIG ===
app = FastAPI(
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,  # Menutup model dengan default
        "defaultModelExpandDepth": -1,  # Menutup model dengan default
        "docExpansion": "none",  # Menutup endpoint
    },
    # docs_url=None,
    # openapi_url=None,
    # redoc_url=None,
)
# app.mount("/static", StaticFiles(directory=DIR_STATIC), name="static")
app.add_middleware(
    CORSMiddleware,
    # Mengizinkan semua origin (bisa dibatasi misalnya ["http://localhost:3000"])
    allow_origins=["*"],
    allow_credentials=True,
    # Mengizinkan semua metode HTTP (GET, POST, PUT, DELETE)
    allow_methods=["GET", "POST", "PUT"],
    allow_headers=["*"],  # Mengizinkan semua header
)
# app.state.limiter = limiter  # slowapi

# === Routes ===
# for route in routes_controller:
#     app.include_router(route)
for route in routes_api:
    app.include_router(route)


# === Error Handling ===
# app.add_exception_handler(RateLimitExceeded, http_code_429)
# app.add_exception_handler(404, http_code_404)
# app.add_exception_handler(500, http_code_500)
