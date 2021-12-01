from fastapi import FastAPI

from config import Config
from apps.libs import register_exception

from .resources import router


def register_routers(app: FastAPI):
    """register routers"""

    app.include_router(router, prefix='/messages', tags=['cars'])


def init_sub_app(app: FastAPI):
    """mount sub app"""

    api_admin_app: FastAPI = FastAPI(include_in_schema=Config.service.INCLUDE_IN_SCHEMA)

    register_exception(api_admin_app)
    register_routers(api_admin_app)
    app.mount(path='/api-sockets', app=api_admin_app, name='api_admin_app')

    return app
