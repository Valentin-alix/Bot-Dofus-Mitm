import logging

from sqlalchemy.orm import sessionmaker

from app.database.models import get_engine, TypeItem, CategoryEnum
from app.gui.signals import AppSignals
from app.modules.hdv.selling_hdv import SellingHdv
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedBidSellerMessage import (
    ExchangeStartedBidSellerMessage,
)
from app.types_.models.common import BotInfo, ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeStartedBidSellerMessageHandler(
    ParsedMessageHandler, ExchangeStartedBidSellerMessage
):
    """Received hdv info seller"""

    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        if len(self.sellerDescriptor.types) > 0:
            engine = get_engine()
            with sessionmaker(bind=engine)() as session:
                category = session.query(TypeItem.category).filter(
                    TypeItem.id == self.sellerDescriptor.types[0]).scalar()
            if category in [CategoryEnum.RESOURCES, CategoryEnum.CONSUMABLES, CategoryEnum.COSMETICS]:
                bot_info.selling_info.selling_hdv = SellingHdv(
                    self.sellerDescriptor, self.objectsInfos, bot_info.selling_info.is_playing_from_inventory_event,
                    bot_info.selling_info.is_playing_update_event,
                    bot_info.common_info,
                    app_signals
                )
                logger.info(f"got hdv seller with types : {self.sellerDescriptor.types}")
                if bot_info.selling_info.is_playing_from_inventory_event.is_set():
                    bot_info.selling_info.selling_hdv.process_from_inventory()
                elif bot_info.selling_info.is_playing_update_event.is_set():
                    bot_info.selling_info.selling_hdv.process_update()
