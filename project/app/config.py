import logging

from pydantic import BaseSettings
from functools import lru_cache

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"  # this is os.getenv("ENVIRONMENT", dev)
    testing: bool = bool(0)


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
