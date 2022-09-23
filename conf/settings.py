from typing import Optional, List

from pydantic import BaseModel


class LogSetting(BaseModel):
    LEVEL: Optional[str] = 'DEBUG'
    PATH: str
    STDOUT: Optional[bool] = True
    ROTATION: Optional[str] = '00:00'
    RETENTION: Optional[str] = '30 days'
    COMPRESSION: Optional[str] = None


class ServiceSetting(BaseModel):
    # openapi swagger
    INCLUDE_IN_SCHEMA: Optional[bool] = True

    # socket.io on
    SOCKET_IO_ON: Optional[bool] = False


class SocketIOSetting(BaseModel):
    SOCKET_IO_NAMESPACES: Optional[List[str]] = ['/']
    SOCKET_IO_MOUNT: Optional[str] = '/'
