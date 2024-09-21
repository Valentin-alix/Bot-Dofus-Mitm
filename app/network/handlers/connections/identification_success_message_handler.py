from datetime import datetime

from app.gui.signals import AppSignals
from app.interfaces.dofus.scripts.com.ankamagames.dofus.network.messages.connection.IdentificationSuccessMessage import (
    IdentificationSuccessMessage,
)
from app.interfaces.models.common import BotInfo, ParsedMessageHandler


class IdentificationSuccessMessageHandler(
    ParsedMessageHandler, IdentificationSuccessMessage
):
    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        bot_info.common_info.subscription_end_date = datetime.fromtimestamp(
            self.subscriptionEndDate / 1000.0
        )
