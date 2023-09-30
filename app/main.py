from fastapi import FastAPI, Depends
from config import (
    get_settings,
    Settings,
)  # can use app.config if depending on the file structure and where it is
from functools import lru_cache

app = FastAPI()


@app.get("/ping")
def pong(
    settings: Settings = Depends(get_settings),
):  # the pong function depends on Depends, which in turn depends on the get_settings functions being run. The settings variable is then set to the returned get_settings value][=[p42 ]]
    print(settings.environment)
    print(settings.testing)

    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testmode": settings.testing,
    }
