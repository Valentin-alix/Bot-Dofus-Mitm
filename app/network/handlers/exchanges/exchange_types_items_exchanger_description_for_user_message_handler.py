import logging
from datetime import datetime

from sqlalchemy.orm import sessionmaker

from app.database.models import Item, Price, get_engine
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
            session = sessionmaker(bind=engine)()
            # Saving prices in database
            item = session.query(Item).filter_by(id=self.objectGID).first()
            with bot_info.common_info.server_id_with_lock["lock"]:
                if item is not None:
                    prices_values = self.itemTypeDescriptions[0].prices
                    price = Price(
                        creation_date=datetime.now(),
                        item_id=item.id,
                        one=prices_values[0],
                        ten=prices_values[1],
                        hundred=prices_values[2],
                        server_id=bot_info.common_info.server_id_with_lock["server_id"],
                    )
                    session.add(price)
                    session.commit()

                    session.close()

        with bot_info.scraping_info.buying_hdv_with_lock.get("lock"):
            if (
                    buying_hdv := bot_info.scraping_info.buying_hdv_with_lock.get(
                        "buying_hdv"
                    )
            ) is not None:
                if bot_info.scraping_info.is_playing_event.is_set():
                    buying_hdv.process()
