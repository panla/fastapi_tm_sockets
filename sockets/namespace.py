import socketio

from extensions import logger


class NameSpaceSIO(socketio.AsyncNamespace):

    async def check(self, sid, msg):
        """check data"""

        if not isinstance(msg, dict):
            logger.error(f'sid {sid} params msg is not dict')
            return await self.disconnect(sid=sid, namespace=self.namespace)

        logger.info(msg)

        room = msg.get('room')
        if not room:
            logger.error(f'sid {sid} the param room is None')
            return await self.disconnect(sid=sid, namespace=self.namespace)

        return f'{room}'

    def on_connect(self, sid):
        """event connect"""

        logger.info(f'sid = {sid} namespace = {self.namespace} build link')

    async def on_disconnect(self, sid):
        """event disconnect"""

        logger.info(f'sid = {sid} namespace = {self.namespace} start disconnect')

        # leave rooms
        rooms = self.rooms(sid=sid, namespace=self.namespace)
        if rooms:
            for room in rooms:
                self.leave_room(sid=sid, room=room, namespace=self.namespace)
        await self.disconnect(sid=sid)

        logger.info(f'sid = {sid} namespace = {self.namespace} over disconnect')

    async def on_join_room(self, sid, msg):
        """event join room"""

        logger.info(f'sid = {sid} namespace = {self.namespace} start join room')

        room = await self.check(sid, msg=msg)
        self.enter_room(sid=sid, room=room, namespace=self.namespace)

        logger.info(f'sid = {sid} namespace = {self.namespace} over join room')

    async def on_leave_room(self, sid, msg):
        """event leave room"""

        logger.info(f'sid = {sid} namespace = {self.namespace} start leave room')

        room = await self.check(sid, msg=msg)
        self.leave_room(sid=sid, room=room, namespace=self.namespace)

        logger.info(f'sid = {sid} namespace = {self.namespace} over leave room')

    async def on_my_event(self, sid, msg):
        """event: my_event"""

        logger.info(f'sid = {sid} namespace = {self.namespace} start my_event')

        room = await self.check(sid, msg=msg)
        await self.emit(event='my_event_response', data=msg, room=room)

        logger.info(f'sid = {sid} namespace = {self.namespace} over my_event')
