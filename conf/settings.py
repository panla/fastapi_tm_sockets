from typing import List

from pydantic import BaseModel


class LogSetting(BaseModel):
    LOG_LEVEL: str = 'DEBUG'
    LOG_PATH: str


class ServiceSetting(BaseModel):
    # openapi swagger
    INCLUDE_IN_SCHEMA: bool = True

    # socket.io on
    SOCKET_IO_ON: bool = False


class SocketIOSetting(BaseModel):
    SOCKET_IO_NAMESPACES: List[str] = ['/']
    SOCKET_IO_MOUNT: str = '/'
