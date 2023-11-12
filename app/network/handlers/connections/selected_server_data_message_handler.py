from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.connection.SelectedServerDataMessage import (
    SelectedServerDataMessage,
)
from app.types_.interface import BotInfo
from app.types_.parsed_message import ParsedMessageHandler


class SelectedServerDataMessageHandler(ParsedMessageHandler, SelectedServerDataMessage):
    def handle(self, bot_info: BotInfo) -> None:
        with bot_info.common_info.server_id_with_lock["lock"]:
            bot_info.common_info.server_id_with_lock["server_id"] = self.serverId
