import enum

from pydantic_settings import BaseSettings

import os
class LogLevel(str, enum.Enum):
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """
    openai_api_key: str = os.getenv('API_KEY')
    fastapi_title: str = "FastApi"
    fastapi_desc: str = "My FastApi test"
    fastapi_version: str = "1.0"
    
    host: str = "localhost"
    port: int = 8000
    uvicorn_reload: bool = True
    # Environment
    # environment: str = "prod"
    log_level: LogLevel = LogLevel.INFO

    class Config:
        extra = 'ignore'
        env_file = "envs/.env"
        env_file_encoding = "utf-8"


settings = Settings()
