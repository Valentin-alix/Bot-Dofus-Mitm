import logging

from app.types_ import BotInfo
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeTypesExchangerDescriptionForUserMessage import (
    ExchangeTypesExchangerDescriptionForUserMessage,
)
from app.types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeTypesExchangerDescriptionForUserMessageHandler(
    ParsedMessageHandler, ExchangeTypesExchangerDescriptionForUserMessage
):
    """Received hdv object types after checking category"""

    def handle(self, bot_info: BotInfo) -> None:
        with bot_info.scraping_info.buying_hdv_with_lock.get("lock"):
            if (
                buying_hdv := bot_info.scraping_info.buying_hdv_with_lock.get(
                    "buying_hdv"
                )
            ) is not None:
                buying_hdv.types_object = [
                    {"object_gid": type_description, "is_opened": False}
                    for type_description in self.typeDescription
                ]
                logger.info("Got type object of category")
                if bot_info.scraping_info.is_playing_event.is_set():
                    buying_hdv.process()
