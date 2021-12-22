from fastapi import FastAPI

from config import ServiceConfig
from apps.libs.init_app import init


def create_app():
    app = FastAPI(include_in_schema=ServiceConfig.INCLUDE_IN_SCHEMA)

    app = init(app)
    return app
