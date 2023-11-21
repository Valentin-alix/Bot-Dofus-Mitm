import logging

from app.gui.signals import AppSignals
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeTypesExchangerDescriptionForUserMessage import (
    ExchangeTypesExchangerDescriptionForUserMessage,
)
from app.types_.models.common import BotInfo, ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeTypesExchangerDescriptionForUserMessageHandler(
    ParsedMessageHandler, ExchangeTypesExchangerDescriptionForUserMessage
):
    """Received hdv object types after checking category"""

    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        assert bot_info.scraping_info.buying_hdv is not None
        bot_info.scraping_info.buying_hdv.objects_left_in_type = [
            {"object_gid": type_description, "is_opened": False}
            for type_description in self.typeDescription
        ]
        logger.info(f"Got type object of category : {self.typeDescription}")
        if bot_info.scraping_info.is_playing_event.is_set():
            bot_info.scraping_info.buying_hdv.process()
