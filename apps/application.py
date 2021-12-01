from fastapi import FastAPI

from apps.libs.init_app import init


def create_app():
    app = FastAPI()

    app = init(app)
    return app
