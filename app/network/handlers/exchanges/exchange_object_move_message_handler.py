from app.gui.signals import AppSignals
from app.interfaces.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMoveMessage import (
    ExchangeObjectMoveMessage,
)
from app.interfaces.models.common import BotInfo, ParsedMessageHandler


class ExchangeObjectMoveMessageHandler(ParsedMessageHandler, ExchangeObjectMoveMessage):
    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        if (selling_hdv := bot_info.selling_info.selling_hdv) is not None:
            selling_hdv.object_on_sale_info = [
                _object
                for _object in selling_hdv.object_on_sale_info
                if _object.objectUID != self.objectUID
            ]
