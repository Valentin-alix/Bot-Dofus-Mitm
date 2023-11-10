import logging
from typing import Tuple

from database.models import Item, TypeItem, get_engine
from sqlalchemy.orm import sessionmaker
from network.utils import send_parsed_msg
from types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHousePriceMessage import (
    ExchangeBidHousePriceMessage,
)
from types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseSearchMessage import (
    ExchangeBidHouseSearchMessage,
)
from types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMovePricedMessage import (
    ExchangeObjectMovePricedMessage,
)
from types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItem import (
    ObjectItem,
)
from types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.SellerBuyerDescriptor import (
    SellerBuyerDescriptor,
)
from types_.interface import SelectedObject, ThreadsInfos

logger = logging.getLogger(__name__)


class SellingHdv:
    def __init__(
        self,
        seller_buyer_descriptor: SellerBuyerDescriptor,
        threads_infos: ThreadsInfos,
    ) -> None:
        self.engine = get_engine()
        self.threads_infos = threads_infos
        self.accepted_categories = seller_buyer_descriptor.types

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
            self.place_object(accepted_objects[-1].objectGID)
        else:
            logger.info("no objects to sell")

    def place_object(self, object_gid: int, do_exchange_bid_house_search: bool = True):
        if do_exchange_bid_house_search:
            send_parsed_msg(
                self.threads_infos,
                ExchangeBidHouseSearchMessage(
                    follow=True,
                    objectGID=object_gid,
                ),
            )
            logger.info(
                f"sending ExchangeBidHouseSearchMessage with objectGID : {object_gid}"
            )
        send_parsed_msg(
            self.threads_infos,
            ExchangeBidHousePriceMessage(
                objectGID=object_gid,
            ),
        )

        logger.info(
            f"sending ExchangeBidHousePriceMessage with objectGID : {object_gid}"
        )

    def sell_selected_object(self):
        if (
            objects_in_inventory := self.get_accepted_objects_in_inventory()
        ) is not None and self.selected_object is not None:
            object_ = next(
                (
                    object_
                    for object_ in objects_in_inventory
                    if object_.objectGID == self.selected_object.get("generic_id")
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
                    send_parsed_msg(
                        self.threads_infos,
                        ExchangeObjectMovePricedMessage(
                            objectUID=object_.objectUID,
                            price=results[1],
                            quantity=results[0],
                        ),
                    )
                    if self.selected_object is not None:
                        self.selected_object["is_placed"] = False
                    # TODO Price is not parsed correctly <!>
                    return
        self.selected_object = None

    # Utils
    def get_name_by_generic_id(self, generic_id: int) -> str | None:
        session = sessionmaker(bind=self.engine)()
        object_ = session.query(Item).filter(Item.id == generic_id).first()
        return object_.name if object_ is not None else None

    def get_object_by_generic_id(self, generic_id: int) -> ObjectItem | None:
        if (accepted_objects := self.get_accepted_objects_in_inventory()) is not None:
            return next(
                (
                    object_
                    for object_ in accepted_objects
                    if object_.objectGID == generic_id
                ),
                None,
            )

    def get_accepted_objects(self):
        session = sessionmaker(bind=self.engine)()
        self.accepted_objects = (
            session.query(Item, TypeItem)
            .join(TypeItem, Item.type_item_id == TypeItem.id)
            .filter(TypeItem.id.in_(self.accepted_categories))
            .with_entities(Item)
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
                    if object_.objectGID
                    in (accepted_object.id for accepted_object in self.accepted_objects)
                ]
                logger.info(
                    f"Get accepted objects in inventory : {accepted_objects_inventory} "
                )
                return accepted_objects_inventory

    def get_price_and_quantity(
        self, _object: ObjectItem, minimal_prices: list[int]
    ) -> Tuple[int, int] | None:
        if _object.quantity >= 100:
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
        elif _object.quantity >= 10:
            quantity = 10
            if minimal_prices[1] != 0:
                price = minimal_prices[1] - 1
            elif minimal_prices[0] != 0:
                price = (minimal_prices[0] * 10) - 1
            else:
                return None
            return quantity, price
        elif _object.quantity >= 1:
            quantity = 1
            if minimal_prices[0] != 0:
                price = minimal_prices[0] - 1
                return quantity, price
            return None
        return None
