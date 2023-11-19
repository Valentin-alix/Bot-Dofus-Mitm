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
        if (
                buying_hdv := bot_info.scraping_info.buying_hdv
        ) is not None:
            buying_hdv.types_object = [
                {"object_gid": type_description, "is_opened": False}
                for type_description in self.typeDescription
            ]
            logger.info("Got type object of category")
            if bot_info.scraping_info.is_playing_event.is_set():
                buying_hdv.process()
