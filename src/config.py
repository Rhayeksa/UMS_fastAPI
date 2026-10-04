import os
import urllib.parse
from pathlib import Path

from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv(dotenv_path="./.env")

# Web
root = Path(__file__).resolve().parents[1]
DIR_STATIC = root / "src" / "static"
templates = root / "src" / "template"
templates = Jinja2Templates(directory=templates)

# JWT
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_ACCESS_TOKEN_EXPIRE_HOURS = os.getenv("JWT_ACCESS_TOKEN_EXPIRE_HOURS", 1)

# PostgreSQL
POSTGRES_USERNAME = os.getenv("POSTGRES_USERNAME", "root")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "root")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "127.0.0.1")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB", "postgres")
POSTGRES_SCHEMA = os.getenv("POSTGRES_SCHEMA", "public")
POSTGRES_SSL_MODE = os.getenv("POSTGRES_SSL_MODE", "").lower()
url = f"postgresql+psycopg2://{POSTGRES_USERNAME}:{urllib.parse.quote_plus(POSTGRES_PASSWORD)}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
if POSTGRES_SSL_MODE in ("require", "verify-ca", "verify-full"):
    url += f"?sslmode={POSTGRES_SSL_MODE}&channel_binding=require"
engine = create_engine(
    url=url,
    pool_size=10,
    max_overflow=5,
    pool_timeout=30,
    pool_pre_ping=True,
    pool_recycle=1800,
)
session = sessionmaker(bind=engine)
session = session()
