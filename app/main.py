from fastapi import FastAPI, Depends
from config import (
    get_settings,
    Settings,
)  # can use app.config if depending on the file structure and where it is

app = FastAPI()


@app.get("/ping")
def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testmode": settings.testing,
    }
