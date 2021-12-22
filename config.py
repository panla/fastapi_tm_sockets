import os
from pathlib import Path
from functools import lru_cache

import pytomlpp
from pydantic import BaseModel

from conf.settings import LogSetting, ServiceSetting, SocketIOSetting


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Setting(BaseModel):
    log: LogSetting
    service: ServiceSetting
    socket_io: SocketIOSetting


@lru_cache()
def get_settings() -> Setting:
    CODE_ENV = os.environ.get('CODE_ENV', 'prd')

    if CODE_ENV == 'test':
        p = Path(BASE_DIR).joinpath('conf/test.local.toml')
    else:
        p = Path(BASE_DIR).joinpath('conf/product.local.toml')

    if not p.is_file():
        raise Exception('config no exists')

    settings = Setting.parse_obj(pytomlpp.load(p))
    return settings


Config = get_settings()

LogConfig = Config.log
ServiceConfig = Config.service
SocketIOConfig = Config.socket_io
