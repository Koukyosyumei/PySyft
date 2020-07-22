from ...common.message import AbstractMessage
from ...common.id import UID
from ...io import Route

class SyftMessage(AbstractMessage):
    def __init__(self, route: Route, msg_id: UID = None) -> None:
        self.route = route
        self.msg_id = msg_id

class SignedMessage(SyftMessage):
    def sign(self, my_route):
        self.my_route = my_route

class SyftMessageWithReply(SignedMessage):
    def __init__(self, route: Route, reply_to: Route, msg_id: UID = None) -> None:
        super(self).__init__(route, msg_id)
        msg.reply_to = reply_to
