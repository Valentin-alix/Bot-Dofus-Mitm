from app.gui.signals import AppSignals
from app.interfaces.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMovePricedMessage import (
    ExchangeObjectMovePricedMessage,
)
from app.interfaces.models.common import BotInfo, ParsedMessageHandler


class ExchangeObjectMovePricedMessageHandler(
    ParsedMessageHandler, ExchangeObjectMovePricedMessage
):
    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None: ...
