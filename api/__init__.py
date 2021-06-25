import os, glob
from fastapi import FastAPI
from .database import engine
# from .routers import blog, user, authentication
# from .routers.authentication import authentication
# from .routers.blog import blog
# from .routers.user import user
# from . import models
# from api.models.blog import Base


def create_app():
    _app = FastAPI()

    # Base.metadata.create_all(bind=engine)
    # user.Base.metadata.create_all(bind=engine)

    """ Modelleri yüklüyoruz """
    names = [os.path.basename(x) for x in glob.glob('api/models/*')]
    for name in names:
        if name != '__pycache__' and name != '__init__.py':
            filename = name.replace('.py','')
            _frommodule = f'api.models.{filename}'
            _temp = __import__(_frommodule, fromlist=['Base'])
            _temp.Base.metadata.create_all(bind=engine)

    """ Route'ları yüklüyoruz """
    for root, dirs, files in os.walk("./api/routers", topdown=True):
        for name in dirs:
            if name != '__pycache__':
                _frommodule = f'api.routers.{name}.{name}'
                _temp = __import__(_frommodule, fromlist=[name])
                object = _temp.router
                _app.include_router(object)
    return _app
