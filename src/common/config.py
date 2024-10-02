import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    # Application settings
    PROJECT_NAME: str = "E-commerce Platform"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    # Database configuration
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "postgresql://postgres:root@localhost/ecommerce_db"
    )

    # JWT configuration
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "supersecretkey")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60  # Token expiry time

    # Other configuration
    ENV: str = os.getenv("ENV", "development")
    EMAIL_SMTP_SERVER: str = os.getenv("EMAIL_SMTP_SERVER", "")
    EMAIL_PORT: int = os.getenv("EMAIL_PORT", 587)


settings = Settings()
