from app.gui.signals import AppSignals
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHousePriceMessage import \
    ExchangeBidHousePriceMessage
from app.types_.models.common import ParsedMessageHandler, BotInfo


class ExchangeBidHousePriceMessageHandler(ParsedMessageHandler, ExchangeBidHousePriceMessage):
    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        if bot_info.selling_info.selling_hdv is not None:
            bot_info.selling_info.selling_hdv.selected_object['is_placed'] = True
