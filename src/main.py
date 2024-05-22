from fastapi import FastAPI

from .routers.comment.router import router as comment_router
from .routers.theme.router import router as theme_router
from .logger import setup_logger


setup_logger('api-main')


app = FastAPI()

app.include_router(comment_router)
app.include_router(theme_router)
