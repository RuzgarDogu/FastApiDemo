import os, glob
from fastapi import FastAPI
from api.utils.database import engine
from .docs_config import docsettings

def create_app():
    _app = FastAPI(
        title=docsettings.title,
        description=docsettings.description,
        version=docsettings.version,
        openapi_tags=docsettings.openapi_tags,
        docs_url=docsettings.docs_url,
        redoc_url=docsettings.redoc_url
    )

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
