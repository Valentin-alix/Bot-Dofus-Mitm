import logging

from app.gui.signals import AppSignals
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.connection.SelectedServerDataMessage import (
    SelectedServerDataMessage,
)
from app.types_.models.common import BotInfo, ParsedMessageHandler

logger = logging.getLogger(__name__)


class SelectedServerDataMessageHandler(ParsedMessageHandler, SelectedServerDataMessage):
    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        bot_info.common_info.server_id = self.serverId
        app_signals.on_new_server_id.emit()
        logger.info(f"Got new serverId : {self.serverId}")
