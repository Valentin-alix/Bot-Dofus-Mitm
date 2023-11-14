import logging
import math
from threading import Thread
from time import sleep
from typing import Tuple

from sqlalchemy.orm import sessionmaker

from app.database.models import Item, TypeItem, get_engine
from app.network.utils import send_parsed_msg
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHousePriceMessage import (
    ExchangeBidHousePriceMessage,
)
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseSearchMessage import (
    ExchangeBidHouseSearchMessage,
)
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMovePricedMessage import \
    ExchangeObjectMovePricedMessage
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItem import (
    ObjectItem,
)
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.SellerBuyerDescriptor import (
    SellerBuyerDescriptor,
)
from app.types_.interface import SelectedObject, BotInfo

logger = logging.getLogger(__name__)


class SellingHdv:
    def __init__(
            self,
            seller_buyer_descriptor: SellerBuyerDescriptor,
            bot_info: BotInfo,
    ) -> None:
        self.engine = get_engine()
        self.bot_info = bot_info
        self.accepted_categories = seller_buyer_descriptor.types

        self.selected_object: SelectedObject | None = None

        self.get_accepted_objects()

        self.is_playing = self.bot_info.selling_info.is_playing_event.is_set()
        self.stop_timer = False
        check_event_play_thread = Thread(target=self.check_event_play, daemon=True)
        check_event_play_thread.start()

    def check_event_play(self):
        """continuously check if event play has changed to true"""
        while (
                not self.bot_info.common_info.is_closed_event.is_set() and not self.stop_timer
        ):
            if (
                    not self.is_playing
                    and self.bot_info.selling_info.is_playing_event.is_set()
            ):
                logger.info("launching selling hdv bot after manual start")
                self.is_playing = True
                self.process()
            self.is_playing = self.bot_info.selling_info.is_playing_event.is_set()
            sleep(2)

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
                self.bot_info,
                ExchangeBidHouseSearchMessage(
                    follow=True,
                    objectGID=object_gid,
                ),
            )
            logger.info(
                f"sending ExchangeBidHouseSearchMessage with objectGID : {object_gid}"
            )
        send_parsed_msg(
            self.bot_info,
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
                    object_.quantity,
                    self.selected_object.get("minimal_prices"),
                )
                logger.info(f"get price_and_quantity : {results}")
                if results is not None:
                    send_parsed_msg(
                        self.bot_info,
                        ExchangeObjectMovePricedMessage(
                            objectUID=object_.objectUID,
                            price=results[1],
                            quantity=results[0],
                        ),
                    )
                    if self.selected_object is not None:
                        self.selected_object["is_placed"] = False
                    return
                else:
                    # TODO Remove in inventory
                    self.selected_object = None
                    self.process()
        else:
            self.selected_object = None

    # Utils
    def get_name_by_generic_id(self, generic_id: int) -> str | None:
        session = sessionmaker(bind=self.engine)()
        object_ = session.query(Item).filter(Item.id == generic_id).first()
        return object_.name if object_ is not None else None

    def get_object_by_generic_id(self, generic_id: int) -> ObjectItem | None:
        # todo voir si vendable
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
        with self.bot_info.common_info.character_with_lock.get("lock"):
            if (
                    character := self.bot_info.common_info.character_with_lock.get(
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
                    f"Get accepted objects in inventory : {[_object.objectGID for _object in accepted_objects_inventory]} "
                )
                return accepted_objects_inventory

    @staticmethod
    def get_price_and_quantity(
            _object_quantity: int, minimal_prices: list[int]
    ) -> Tuple[int, int] | None:
        if _object_quantity >= 100:
            quantity = 100
        elif _object_quantity >= 10:
            quantity = 10
        elif _object_quantity >= 1:
            quantity = 1
        else:
            return None

        price = None
        for index, _price in enumerate(minimal_prices):
            if _price != 0:
                current_quantity = int(f"1{str(0) * index}")
                price = _price / current_quantity
                if current_quantity == quantity:
                    break
        if price is None:
            return None
        price_for_quantity = math.ceil(price * quantity)

        return quantity, price_for_quantity
