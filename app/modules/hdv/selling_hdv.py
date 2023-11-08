import logging
from typing import Tuple, TypedDict

from database.models import Object, TypeObject, get_engine
from network.parsed_message.dicts import ObjectItem, SellerBuyerDescriptor
from network.parsed_message.parsed_message_client.exchanges.exchange_bid_house_price_message import (
    ExchangeBidHousePriceMessage,
)
from network.parsed_message.parsed_message_client.exchanges.exchange_bid_house_search_message import (
    ExchangeBidHouseSearchMessage,
)
from network.parsed_message.parsed_message_client.exchanges.exchange_object_move_priced_message import (
    ExchangeObjectMovePricedMessage,
)
from sqlalchemy.orm import sessionmaker
from types_.interface import ThreadsInfos

logger = logging.getLogger(__name__)


class SelectedObject(TypedDict):
    all_identical: bool
    generic_id: int
    minimal_prices: list[int]
    is_placed: bool


class SellingHdv:
    def __init__(
        self,
        seller_buyer_descriptor: SellerBuyerDescriptor,
        threads_infos: ThreadsInfos,
    ) -> None:
        self.engine = get_engine()
        self.threads_infos = threads_infos
        self.accepted_categories = seller_buyer_descriptor.get("types")

        self.selected_object: SelectedObject | None = None

        self.get_accepted_objects()

    def process(self) -> None:
        if self.selected_object is not None:
            if self.selected_object.get("is_placed"):
                self.sell_selected_object()
            else:
                self.place_object(self.selected_object.get("generic_id"), False)
        elif (
            accepted_objects := self.get_accepted_objects_in_inventory()
        ) is not None and len(accepted_objects) > 0:
            self.place_object(accepted_objects[-1].get("objectGID"))
        else:
            logger.info("no objects to sell")

    def place_object(self, object_gid: int, do_exchange_bid_house_search: bool = True):
        if do_exchange_bid_house_search:
            exchange_bid_house_search_message = ExchangeBidHouseSearchMessage(
                __type__="ExchangeBidHouseSearchMessage",
                from_client=True,
                follow=True,
                objectGID=object_gid,
            )
            logger.info(
                f"sending ExchangeBidHouseSearchMessage with objectGID : {object_gid}"
            )
            exchange_bid_house_search_message.send(self.threads_infos)
        exchange_bid_house_price_message = ExchangeBidHousePriceMessage(
            __type__="ExchangeBidHousePriceMessage",
            from_client=True,
            objectGID=object_gid,
        )

        logger.info(
            f"sending ExchangeBidHousePriceMessage with objectGID : {object_gid}"
        )
        exchange_bid_house_price_message.send(self.threads_infos)

    def sell_selected_object(self):
        if (
            objects_in_inventory := self.get_accepted_objects_in_inventory()
        ) is not None and self.selected_object is not None:
            object_ = next(
                (
                    object_
                    for object_ in objects_in_inventory
                    if object_.get("objectGID")
                    == self.selected_object.get("generic_id")
                ),
                None,
            )
            if object_ is not None:
                results = self.get_price_and_quantity(
                    object_,
                    self.selected_object.get("minimal_prices"),
                )
                logger.info(f"get price_and_quantity : {results}")
                if results is not None:
                    exchange_object_move_priced_message = (
                        ExchangeObjectMovePricedMessage(
                            __type__="ExchangeObjectMovePricedMessage",
                            from_client=True,
                            objectUID=object_.get("objectUID"),
                            price=results[1],
                            quantity=results[0],
                        )
                    )
                    logger.info(
                        f"sending ExchangeObjectMovePricedMessage {str(exchange_object_move_priced_message)}"
                    )
                    if self.selected_object is not None:
                        self.selected_object["is_placed"] = False
                    # TODO Price is not parsed correctly <!>
                    return
                    exchange_object_move_priced_message.send(self.threads_infos)
                    return
        self.selected_object = None

    # Utils
    def get_object_by_generic_id(self, generic_id: int) -> ObjectItem | None:
        if (accepted_objects := self.get_accepted_objects_in_inventory()) is not None:
            return next(
                (
                    object_
                    for object_ in accepted_objects
                    if object_.get("objectGID") == generic_id
                ),
                None,
            )

    def get_accepted_objects(self):
        session = sessionmaker(bind=self.engine)()
        self.accepted_objects = (
            session.query(Object, TypeObject)
            .join(TypeObject, Object.type_object_id == TypeObject.id)
            .filter(TypeObject.type_id.in_(self.accepted_categories))
            .with_entities(Object)
            .all()
        )
        session.close()

    def get_accepted_objects_in_inventory(self) -> list[ObjectItem] | None:
        with self.threads_infos.get("character_with_lock").get("lock"):
            if (
                character := self.threads_infos.get("character_with_lock").get(
                    "character"
                )
            ) is not None:
                accepted_objects_inventory = [
                    object_
                    for object_ in character.objects
                    if object_.get("objectGID")
                    in (
                        accepted_object.object_gid
                        for accepted_object in self.accepted_objects
                    )
                ]
                logger.info(
                    f"Get accepted objects in inventory : {accepted_objects_inventory} "
                )
                return accepted_objects_inventory

    def get_price_and_quantity(
        self, _object: ObjectItem, minimal_prices: list[int]
    ) -> Tuple[int, int] | None:
        if _object.get("quantity") >= 100:
            quantity = 100
            if minimal_prices[2] != 0:
                price = minimal_prices[2] - 1
            elif minimal_prices[1] != 0:
                price = (minimal_prices[1] * 10) - 1
            elif minimal_prices[0] != 0:
                price = (minimal_prices[0] * 100) - 1
            else:
                return None
            return quantity, price
        elif _object.get("quantity") >= 10:
            quantity = 10
            if minimal_prices[1] != 0:
                price = minimal_prices[1] - 1
            elif minimal_prices[0] != 0:
                price = (minimal_prices[0] * 10) - 1
            else:
                return None
            return quantity, price
        elif _object.get("quantity") >= 1:
            quantity = 1
            if minimal_prices[0] != 0:
                price = minimal_prices[0] - 1
                return quantity, price
            return None
        return None
