from functools import lru_cache
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    loglevel: Optional[str] = os.environ.get("LOGLEVEL")
    secret_key: str = os.environ.get("JWT_SECRET")
    # algorithm: str = os.environ.get("ALGORITHM")
    postgres_db: str = os.environ.get("POSTGRES_DB")
    postgres_user: str = os.environ.get("POSTGRES_USER")
    postgres_password: str = os.environ.get("POSTGRES_PASSWORD")
    postgres_host: str = os.environ.get("POSTGRES_HOST")
    postgres_port: int = os.environ.get("POSTGRES_PORT")
    secret_code: str = os.environ.get("SECRET_CODE")


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
