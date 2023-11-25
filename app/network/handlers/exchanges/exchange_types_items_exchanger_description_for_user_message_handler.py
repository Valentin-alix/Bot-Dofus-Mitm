import logging
from datetime import datetime

from sqlalchemy.orm import sessionmaker

from app.database.models import Price, get_engine
from app.gui.signals import AppSignals
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeTypesItemsExchangerDescriptionForUserMessage import (
    ExchangeTypesItemsExchangerDescriptionForUserMessage,
)
from app.types_.models.common import BotInfo, ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeTypesItemsExchangerDescriptionForUserMessageHandler(
    ParsedMessageHandler, ExchangeTypesItemsExchangerDescriptionForUserMessage
):
    """Received hdv object prices after clicking in objects"""

    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        if len(self.itemTypeDescriptions) >= 1:
            lowest_price_item_unity = min([_item.prices[0] for _item in self.itemTypeDescriptions])
            lowest_price_item_ten = min([_item.prices[1] for _item in self.itemTypeDescriptions])
            lowest_price_item_hundred = min([_item.prices[2] for _item in self.itemTypeDescriptions])

            # storing prices in database
            engine = get_engine()
            logger.info(f"Got minimal prices of objects : {self.itemTypeDescriptions[0]}")
            with sessionmaker(bind=engine)() as session:
                price = Price(
                    creation_date=datetime.now(),
                    item_id=self.objectGID,
                    one=lowest_price_item_unity,
                    ten=lowest_price_item_ten,
                    hundred=lowest_price_item_hundred,
                    server_id=bot_info.common_info.server_id,
                )
                session.add(price)
                session.commit()

        if (
                buying_hdv := bot_info.scraping_info.buying_hdv
        ) is not None and bot_info.scraping_info.is_playing_event.is_set():
            buying_hdv.process()
