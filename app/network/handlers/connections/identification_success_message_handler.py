from datetime import datetime, UTC

from app.gui.signals import AppSignals
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.connection.IdentificationSuccessMessage import \
    IdentificationSuccessMessage
from app.types_.models.common import ParsedMessageHandler, BotInfo


class IdentificationSuccessMessageHandler(ParsedMessageHandler, IdentificationSuccessMessage):
    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        bot_info.common_info.subscription_end_date = datetime.fromtimestamp(self.subscriptionEndDate / 1000.0, UTC)
