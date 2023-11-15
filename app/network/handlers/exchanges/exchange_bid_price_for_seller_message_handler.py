import logging

from app.types_ import BotInfo
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidPriceForSellerMessage import (
    ExchangeBidPriceForSellerMessage,
)
from app.types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeBidPriceForSellerMessageHandler(
    ParsedMessageHandler, ExchangeBidPriceForSellerMessage
):
    """When selecting object for sells"""

    def handle(self, bot_info: BotInfo) -> None:
        with bot_info.selling_info.selling_hdv_with_lock.get("lock"):
            if (
                selling_hdv := bot_info.selling_info.selling_hdv_with_lock.get(
                    "selling_hdv"
                )
            ) is not None:
                logger.info("get selected object")

                with bot_info.common_info.character_with_lock.get("lock"):
                    _object_in_inventory = next(
                        (
                            _object
                            for _object in bot_info.common_info.character_with_lock[
                                "character"
                            ].objects
                            if _object.objectGID == self.genericId
                        ),
                        None,
                    )
                    if _object_in_inventory is not None:
                        selling_hdv.selected_object = {
                            "quantity": _object_in_inventory.quantity,
                            "all_identical": self.allIdentical,
                            "object_gid": self.genericId,
                            "object_uid": _object_in_inventory.objectUID,
                            "is_placed": True,
                            "minimal_prices": self.minimalPrices,
                        }
                if bot_info.selling_info.is_playing_event.is_set():
                    selling_hdv.process()
            else:
                raise ValueError("SellerHdv should not be None")
