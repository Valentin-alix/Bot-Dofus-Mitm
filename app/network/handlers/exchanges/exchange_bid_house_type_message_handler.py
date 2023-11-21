from app.gui.signals import AppSignals
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseTypeMessage import \
    ExchangeBidHouseTypeMessage
from app.types_.models.common import ParsedMessageHandler, BotInfo


class ExchangeBidHouseTypeMessageHandler(ParsedMessageHandler, ExchangeBidHouseTypeMessage):
    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        if bot_info.scraping_info.is_playing_event.is_set():
            assert bot_info.scraping_info.buying_hdv is not None
            if self.follow is True:
                bot_info.scraping_info.buying_hdv.selected_type = self.type
            else:
                bot_info.scraping_info.buying_hdv.selected_type = None
                bot_info.scraping_info.buying_hdv.process()
