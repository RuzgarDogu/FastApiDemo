import os
from fastapi import FastAPI
from .database import engine
# from .routers import blog, user, authentication
# from .routers.authentication import authentication
# from .routers.blog import blog
# from .routers.user import user
from . import models

def create_app():
    _app = FastAPI()
    models.Base.metadata.create_all(bind=engine)

    for root, dirs, files in os.walk("./blog/routers", topdown=True):
        for name in dirs:
            if name != '__pycache__':
                _frommodule = f'blog.routers.{name}.{name}'
                _temp = __import__(_frommodule, fromlist=[name])
                object = _temp.router
                _app.include_router(object)
    return _app
