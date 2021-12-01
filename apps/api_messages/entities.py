from typing import Optional, Any

from fastapi import Body
from pydantic import BaseModel


class SchemaMixin(BaseModel):
    status_code: int = 10000
    message: str = ''
    data: Optional[Any]


class MyEventMessageParser(BaseModel):
    room: int = Body(..., title='room', ge=1)
    user_id: int = Body(..., title='user.id', ge=1)


class MyEventSchema(SchemaMixin):
    data: bool = True
