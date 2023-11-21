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
        # TODO Why itemTypeDescriptions is list
        if len(self.itemTypeDescriptions) == 1:
            # storing prices in database
            engine = get_engine()
            logger.info(f"Got prices of objects : {self.itemTypeDescriptions[0]}")
            with sessionmaker(bind=engine)() as session:
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

        if (
                buying_hdv := bot_info.scraping_info.buying_hdv
        ) is not None and bot_info.scraping_info.is_playing_event.is_set():
            buying_hdv.process()
