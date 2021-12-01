from typing import List

from pydantic import BaseModel


class LogConfig(BaseModel):
    LOG_LEVEL: str = 'DEBUG'
    LOG_PATH: str


class ServiceConfig(BaseModel):
    # openapi swagger
    INCLUDE_IN_SCHEMA: bool = True

    # socket.io on
    SOCKET_IO_ON: bool = False


class SocketIOConfig(BaseModel):
    SOCKET_IO_NAMESPACES: List[str] = ['/']
    SOCKET_IO_MOUNT: str = '/'
