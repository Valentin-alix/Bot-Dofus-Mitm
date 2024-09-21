import logging

from app.database.models import CategoryEnum, TypeItem
from app.database.utils import SessionLocal
from app.gui.signals import AppSignals
from app.interfaces.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedBidSellerMessage import (
    ExchangeStartedBidSellerMessage,
)
from app.interfaces.models.common import BotInfo, ParsedMessageHandler
from app.modules.selling_sale_hotel import SellingSaleHotel

logger = logging.getLogger(__name__)


class ExchangeStartedBidSellerMessageHandler(
    ParsedMessageHandler, ExchangeStartedBidSellerMessage
):
    """Received hdv info seller"""

    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        if len(self.sellerDescriptor.types) > 0:
            with SessionLocal() as session:
                category = (
                    session.query(TypeItem.category)
                    .filter(TypeItem.id == self.sellerDescriptor.types[0])
                    .scalar()
                )
            if category in [
                CategoryEnum.RESOURCES,
                CategoryEnum.CONSUMABLES,
                CategoryEnum.COSMETICS,
            ]:
                bot_info.selling_info.selling_hdv = SellingSaleHotel(
                    self.sellerDescriptor,
                    self.objectsInfos,
                    bot_info.selling_info.is_playing_from_inventory_event,
                    bot_info.selling_info.is_playing_update_event,
                    bot_info.common_info,
                    app_signals,
                )
                logger.info(
                    f"got hdv seller with types : {self.sellerDescriptor.types}"
                )
                if bot_info.selling_info.is_playing_from_inventory_event.is_set():
                    bot_info.selling_info.selling_hdv.process_from_inventory()
                elif bot_info.selling_info.is_playing_update_event.is_set():
                    bot_info.selling_info.selling_hdv.process_update()
