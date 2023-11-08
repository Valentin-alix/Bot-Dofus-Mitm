import logging

from modules.character import Character
from modules.hdv.buying_hdv import BuyingHdv
from modules.hdv.selling_hdv import SellingHdv
from network.parsed_message.parsed_message_client.exchanges.exchange_bid_house_price_message import (
    ExchangeBidHousePriceMessage,
)
from network.parsed_message.parsed_message_client.exchanges.exchange_bid_house_search_message import (
    ExchangeBidHouseSearchMessage,
)
from network.parsed_message.parsed_message_client.exchanges.exchange_bid_house_type_message import (
    ExchangeBidHouseTypeMessage,
)
from network.parsed_message.parsed_message_client.exchanges.exchange_object_move_priced_message import (
    ExchangeObjectMovePricedMessage,
)
from network.parsed_message.parsed_message_server.exchanges.exchange_bid_house_item_add_ok_message import (
    ExchangeBidHouseItemAddOkMessage,
)
from network.parsed_message.parsed_message_server.exchanges.exchange_bid_price_for_seller_message import (
    ExchangeBidPriceForSellerMessage,
)
from network.parsed_message.parsed_message_server.exchanges.exchange_leave_message import (
    ExchangeLeaveMessage,
)
from network.parsed_message.parsed_message_server.exchanges.exchange_started_bid_buyer_message import (
    ExchangeStartedBidBuyerMessage,
)
from network.parsed_message.parsed_message_server.exchanges.exchange_started_bid_seller_message import (
    ExchangeStartedBidSellerMessage,
)
from network.parsed_message.parsed_message_server.exchanges.exchange_types_exchanger_description_for_user_message import (
    ExchangeTypesExchangerDescriptionForUserMessage,
)
from network.parsed_message.parsed_message_server.exchanges.exchange_types_items_exchanger_description_for_user_message import (
    ExchangeTypesItemsExchangerDescriptionForUserMessage,
)
from network.parsed_message.parsed_message_server.inventory.inventory_content_message import (
    InventoryContentMessage,
)
from network.parsed_message.parsed_message_server.inventory.object_added_message import (
    ObjectAddedMessage,
)
from network.parsed_message.parsed_message_server.inventory.object_deleted_message import (
    ObjectDeletedMessage,
)
from network.parsed_message.parsed_message_server.inventory.object_quantity_message import (
    ObjectQuantityMessage,
)
from network.parsed_message.parsed_message_server.parsed_message_server import (
    ParsedMessageServer,
)
from types_ import ParsedMessage, ThreadsInfos

logger = logging.getLogger(__name__)


class Handler:
    parsed_message_class_by_types: dict[str, type[ParsedMessage]] = {
        "ExchangeBidHousePriceMessage": ExchangeBidHousePriceMessage,
        "ExchangeBidHouseSearchMessage": ExchangeBidHouseSearchMessage,
        "ExchangeBidHouseTypeMessage": ExchangeBidHouseTypeMessage,
        "ExchangeBidPriceForSellerMessage": ExchangeBidPriceForSellerMessage,
        "ExchangeLeaveMessage": ExchangeLeaveMessage,
        "ExchangeObjectMovePricedMessage": ExchangeObjectMovePricedMessage,
        "ExchangeStartedBidBuyerMessage": ExchangeStartedBidBuyerMessage,
        "ExchangeStartedBidSellerMessage": ExchangeStartedBidSellerMessage,
        "ExchangeTypesExchangerDescriptionForUserMessage": ExchangeTypesExchangerDescriptionForUserMessage,
        "ExchangeTypesItemsExchangerDescriptionForUserMessage": ExchangeTypesItemsExchangerDescriptionForUserMessage,
        "InventoryContentMessage": InventoryContentMessage,
        "ObjectAddedMessage": ObjectAddedMessage,
        "ObjectDeletedMessage": ObjectDeletedMessage,
        "ObjectQuantityMessage": ObjectQuantityMessage,
        "ExchangeBidHouseItemAddOkMessage": ExchangeBidHouseItemAddOkMessage,
    }

    def __init__(self, threads_infos: ThreadsInfos) -> None:
        self.buying_hdv: BuyingHdv | None = None
        self.selling_hdv: SellingHdv | None = None
        self.character: Character | None = None
        self.threads_infos = threads_infos

    def handle_message_unpacked(self, parsed_message: ParsedMessage):
        if self.threads_infos.get("event_play_sniffer").is_set():
            self.threads_infos.get("queue_handler_message").put(parsed_message)

        if (
            parsed_msg_class := self.parsed_message_class_by_types.get(
                parsed_message.__type__
            )
        ) is not None:
            parsed_msg_instance = parsed_msg_class(**vars(parsed_message))
            if isinstance(parsed_msg_instance, ParsedMessageServer):
                parsed_msg_instance.handle(self.threads_infos)
