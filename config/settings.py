from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    QDRANT_URL: Optional[str] = None
    QDRANT_PORT: Optional[int] = None

settings = Settings()
