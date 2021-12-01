from fastapi import APIRouter

from extensions import Route, error_response, resp_success, SocketDefine
from apps.api_messages.entities import MyEventMessageParser, MyEventSchema
from sockets.server import socket_io

router = APIRouter(route_class=Route, responses=error_response)


@router.post('/my_event', response_model=MyEventSchema, status_code=201)
async def send_my_event_message(parser: MyEventMessageParser):

    params = parser.dict()

    room = params.get('room')

    await socket_io.emit(event=SocketDefine.event, data=params, room=f'{room}', namespace=SocketDefine.namespace)

    return resp_success(data=True)
