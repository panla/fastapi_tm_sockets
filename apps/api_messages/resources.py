from fastapi import APIRouter

from extensions import Route, ErrorSchema
from conf.const import SocketConst
from apps.api_messages.entities import MyEventMessageParser, MyEventSchema
from sockets.server import socket_io

router = APIRouter(route_class=Route, responses=ErrorSchema)


@router.post('/my_event', response_model=MyEventSchema, status_code=201)
async def send_my_event_message(parser: MyEventMessageParser):

    room = parser.room
    await socket_io.emit(event=SocketConst.EVENT, data=parser.dict(), room=f'{room}', namespace=SocketConst.NAMESPACE)

    return MyEventSchema(data=True)
