import logging
import math
from threading import Thread
from time import sleep
from typing import Tuple, Type

from sqlalchemy.orm import sessionmaker

from app.database.models import Item, TypeItem, get_engine
from app.network.utils import send_parsed_msg
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHousePriceMessage import (
    ExchangeBidHousePriceMessage,
)
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseSearchMessage import (
    ExchangeBidHouseSearchMessage,
)
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMovePricedMessage import (
    ExchangeObjectMovePricedMessage,
)
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

        self.accepted_categories: list[int] = seller_buyer_descriptor.types
        self.accepted_objects = self.get_accepted_objects()

        self.treated_objects: list[int] = []

        self.selected_object: SelectedObject | None = None

        # TODO Use signal instead
        self.is_playing = self.bot_info.selling_info.is_playing_event.is_set()
        self.stop_timer = False
        check_event_play_thread = Thread(target=self.check_event_play, daemon=True)
        check_event_play_thread.start()

    def check_event_play(self):
        """continuously check if event play has changed to true"""
        while not self.stop_timer:
            if (
                    not self.is_playing
                    and self.bot_info.selling_info.is_playing_event.is_set()
            ):
                logger.info("launching selling hdv bot after manual start")
                self.process()
            self.is_playing = self.bot_info.selling_info.is_playing_event.is_set()
            sleep(2)

    def process(self) -> None:
        if self.selected_object is not None and self.selected_object["quantity"] != 0:
            if self.selected_object.get("is_placed"):
                self.sell_selected_object()
            else:
                self.place_object(self.selected_object["object_gid"], False)
        elif (
                accepted_objects_in_inventory := self.get_accepted_objects_in_inventory()
        ) is not None and len(accepted_objects_in_inventory) > 0:
            self.place_object(accepted_objects_in_inventory[-1].objectGID)
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
        if self.selected_object is not None:
            results = self.get_price_and_quantity(
                self.selected_object["quantity"],
                self.selected_object.get("minimal_prices"),
            )
            logger.info(f"get price_and_quantity : {results}")
            if results is not None:
                logger.info(
                    f"send ExchangeObjectMovePricedMessage {self.selected_object['object_uid']}"
                )
                send_parsed_msg(
                    self.bot_info,
                    ExchangeObjectMovePricedMessage(
                        objectUID=self.selected_object["object_uid"],
                        price=results[1],
                        quantity=results[0],
                    ),
                )
                self.selected_object["is_placed"] = False
                self.selected_object["quantity"] -= results[0]
                return
            else:
                logger.info("result is none, cleaning inventory from object...")
                self.treated_objects.append(self.selected_object["object_gid"])

                send_parsed_msg(
                    self.bot_info,
                    ExchangeBidHouseSearchMessage(
                        follow=False,
                        objectGID=self.selected_object["object_gid"],
                    ),
                )
                logger.info(
                    f"sending ExchangeBidHouseSearchMessage with objectGID : {self.selected_object['object_gid']} to "
                    f"close"
                )
                self.selected_object = None
                self.process()
        else:
            raise ValueError("selected object should not be None")

    # Utils
    def get_accepted_objects(self) -> list[Type[Item]]:
        with sessionmaker(bind=self.engine)() as _session:
            accepted_objects: list[Type[Item]] = (
                _session.query(Item)
                .join(TypeItem, Item.type_item_id == TypeItem.id)
                .filter(TypeItem.id.in_(self.accepted_categories))
                .with_entities(Item)
                .all()
            )
            return accepted_objects

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
                       and object_.objectGID not in self.treated_objects
                ]
                logger.info(
                    f"Get accepted objects in inventory : {[_object.objectGID for _object in accepted_objects_inventory]}"
                )
                return accepted_objects_inventory
            else:
                raise ValueError("character should not be None")

    @staticmethod
    def get_price_and_quantity(
            _object_quantity: int, minimal_prices: list[int]
    ) -> Tuple[int, int] | None:
        if _object_quantity == 0:
            return None

        quantity = int(f"1{str(0) * min((len(str(_object_quantity)) - 1), 2)}")

        price = None
        for index, _price in enumerate(minimal_prices):
            if _price > 1:
                current_quantity = int(f"1{str(0) * index}")
                price = _price / current_quantity
                if current_quantity == quantity:
                    break
        if price is None:
            return None

        return quantity, math.ceil(price * quantity)
