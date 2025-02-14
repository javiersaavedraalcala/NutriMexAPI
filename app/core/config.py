from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Basic API config
    PROJECT_NAME: str = "NutriMexAPI"
    API_V1_STR: str = "/api/v1"

    # Database config
    DATABASE_URL: str

    # Security config
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

# Create a config instance
settings = Settings()