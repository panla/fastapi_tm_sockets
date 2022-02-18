from typing import Any

from extensions import logger
from conf.const import StatusCode




def resp_success(code: int = StatusCode.success, message: str = '', print_msg: str = '', data: Any = None):
    if print_msg:
        pass
    else:
        if message and message != 'success':
            print_msg = message

    if print_msg:
        logger.info(print_msg)

    return {'code': StatusCode.success, 'message': message, 'data': data}
