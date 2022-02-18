from typing import Optional, List

from pydantic import BaseModel


class LogSetting(BaseModel):
    LOG_LEVEL: Optional[str] = 'DEBUG'
    LOG_PATH: str


class ServiceSetting(BaseModel):
    # openapi swagger
    INCLUDE_IN_SCHEMA: Optional[bool] = True

    # socket.io on
    SOCKET_IO_ON: Optional[bool] = False


class SocketIOSetting(BaseModel):
    SOCKET_IO_NAMESPACES: Optional[List[str]] = ['/']
    SOCKET_IO_MOUNT: Optional[str] = '/'
