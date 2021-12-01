from fastapi import FastAPI

from apps.api_messages import init_sub_app as init_api_messages_app
from sockets.server import init_sub_app as init_sockets_app


def init(app: FastAPI):

    init_api_messages_app(app)
    app = init_sockets_app(app)

    return app
