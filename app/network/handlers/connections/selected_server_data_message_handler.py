import logging

from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.connection.SelectedServerDataMessage import (
    SelectedServerDataMessage,
)
from app.types_.interface import BotInfo
from app.types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class SelectedServerDataMessageHandler(ParsedMessageHandler, SelectedServerDataMessage):
    def handle(self, bot_info: BotInfo) -> None:
        bot_info.common_info.server_id = self.serverId
        logger.info(f"Got new serverId : {self.serverId}")
