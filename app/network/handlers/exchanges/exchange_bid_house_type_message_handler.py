from app.gui.signals import AppSignals
from app.interfaces.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseTypeMessage import (
    ExchangeBidHouseTypeMessage,
)
from app.interfaces.models.common import BotInfo, ParsedMessageHandler


class ExchangeBidHouseTypeMessageHandler(
    ParsedMessageHandler, ExchangeBidHouseTypeMessage
):
    """from client, when selecting type in hdv"""

    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        if bot_info.scraping_info.is_playing_event.is_set():
            if self.follow is True:
                bot_info.scraping_info.buying_hdv.selected_type = self.type
            else:
                bot_info.scraping_info.buying_hdv.selected_type = None
