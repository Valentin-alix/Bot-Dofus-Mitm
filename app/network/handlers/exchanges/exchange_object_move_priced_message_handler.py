from app.gui.signals import AppSignals
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMovePricedMessage import (
    ExchangeObjectMovePricedMessage,
)
from app.types_.models.common import ParsedMessageHandler, BotInfo


class ExchangeObjectMovePricedMessageHandler(
    ParsedMessageHandler, ExchangeObjectMovePricedMessage
):
    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        ...
