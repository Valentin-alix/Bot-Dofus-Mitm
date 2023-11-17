import logging
from datetime import datetime

from sqlalchemy.orm import sessionmaker

from app.database.models import Price, get_engine
from app.types_ import BotInfo
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeTypesItemsExchangerDescriptionForUserMessage import (
    ExchangeTypesItemsExchangerDescriptionForUserMessage,
)
from app.types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeTypesItemsExchangerDescriptionForUserMessageHandler(
    ParsedMessageHandler, ExchangeTypesItemsExchangerDescriptionForUserMessage
):
    """Received hdv object prices after clicking in objects"""

    def handle(self, bot_info: BotInfo) -> None:
        logger.info("Got prices of objects")
        if len(self.itemTypeDescriptions) == 1:
            engine = get_engine()

            with sessionmaker(
                    bind=engine
            )() as session:
                price = Price(
                    creation_date=datetime.now(),
                    item_id=self.objectGID,
                    one=self.itemTypeDescriptions[0].prices[0],
                    ten=self.itemTypeDescriptions[0].prices[1],
                    hundred=self.itemTypeDescriptions[0].prices[2],
                    server_id=bot_info.common_info.server_id,
                )
                session.add(price)
                session.commit()

        with bot_info.scraping_info.buying_hdv_with_lock.get("lock"):
            if (
                    buying_hdv := bot_info.scraping_info.buying_hdv_with_lock.get(
                        "buying_hdv"
                    )
            ) is not None and bot_info.scraping_info.is_playing_event.is_set():
                buying_hdv.process()
