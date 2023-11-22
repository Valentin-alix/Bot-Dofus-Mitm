from __future__ import annotations

import logging
import math
from copy import deepcopy
from datetime import datetime
from threading import Event, Thread
from typing import Tuple, TYPE_CHECKING

from sqlalchemy.orm import sessionmaker

from app.database.models import Item, TypeItem, get_engine
from app.modules.hdv.hdv import Hdv
from app.network.utils import send_parsed_msg
from app.types_.dicts.common import EventValueChangeWithCallback
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHousePriceMessage import (
    ExchangeBidHousePriceMessage,
)
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectModifyPricedMessage import (
    ExchangeObjectModifyPricedMessage,
)
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMovePricedMessage import (
    ExchangeObjectMovePricedMessage,
)
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItem import (
    ObjectItem,
)
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInBid import (
    ObjectItemToSellInBid,
)
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.SellerBuyerDescriptor import (
    SellerBuyerDescriptor,
)

if TYPE_CHECKING:
    from app.types_.models.common import CommonInfo

logger = logging.getLogger(__name__)


class SellingHdv(Hdv):
    def __init__(
            self,
            seller_buyer_descriptor: SellerBuyerDescriptor,
            object_on_sale_info: list[ObjectItemToSellInBid],
            is_playing_from_inventory_event: Event,
            is_playing_update_event: Event,
            common_info: CommonInfo,
    ) -> None:
        super().__init__(common_info)
        self.engine = get_engine()

        self.is_playing_from_inventory_event = is_playing_from_inventory_event
        self.is_playing_update_event = is_playing_update_event

        self.accepted_objects_type: list[int] = seller_buyer_descriptor.types
        self.accepted_objects_gid = self.get_accepted_objects()
        self.object_on_sale_info = [
            _object
            for _object in object_on_sale_info
            if _object.objectGID in self.accepted_objects_gid
        ]
        self.objects_to_update: list[ObjectItemToSellInBid] = deepcopy(
            object_on_sale_info
        )
        self.treated_objects_in_inventory: list[int] = []

        if self.is_playing_update_event.is_set():
            self.on_start_update(True)
        elif self.is_playing_from_inventory_event.is_set():
            self.on_start_inventory(True)
        else:
            self.on_stop(True)

    def on_stop(self, is_first: bool = False):
        if not is_first and self.selected_object is not None:
            self.close_selected_object()
        check_event_play_inventory_thread = Thread(
            target=lambda: self.check_event_play(
                EventValueChangeWithCallback(
                    target_value=True,
                    event=self.is_playing_from_inventory_event,
                    callback=self.on_start_inventory,
                )), daemon=True)
        check_event_play_inventory_thread.start()

        check_event_play_update_thread = Thread(
            target=lambda: self.check_event_play(
                EventValueChangeWithCallback(
                    target_value=True,
                    event=self.is_playing_update_event,
                    callback=self.on_start_update,
                )), daemon=True)
        check_event_play_update_thread.start()

    def on_start_inventory(self, is_first: bool = False):
        if not is_first:
            self.process_from_inventory()
        check_event_play_update_thread = Thread(
            target=lambda: self.check_event_play(
                EventValueChangeWithCallback(
                    target_value=False,
                    event=self.is_playing_from_inventory_event,
                    callback=self.on_stop,
                )), daemon=True)
        check_event_play_update_thread.start()

    def on_start_update(self, is_first: bool = False):
        if not is_first:
            self.process_update()
        check_event_play_update_thread = Thread(
            target=lambda: self.check_event_play(
                EventValueChangeWithCallback(
                    target_value=False,
                    event=self.is_playing_update_event,
                    callback=self.on_stop,
                )), daemon=True)
        check_event_play_update_thread.start()

    def process_update(self) -> None:
        if self.selected_object is not None:
            self.update_price_selected_object()
        elif len(self.objects_to_update) > 0:
            self.place_object(self.objects_to_update[0].objectGID, True)
        else:
            logger.info("no object left to update")

    def process_from_inventory(self) -> None:
        if (
                self.selected_object is not None
                and self.get_quantity_in_inventory(self.selected_object["object_gid"])
                != 0
        ):
            if self.selected_object["is_placed"]:
                self.sell_selected_object()
            else:
                self.place_object(self.selected_object["object_gid"], False)
        elif self.selected_object is not None:
            self.close_selected_object()
        elif (_object := self.get_accepted_object_in_inventory()) is not None:
            self.place_object(_object.objectGID)
        else:
            logger.info("no object left to sell")

    def place_object(self, object_gid: int, do_exchange_bid_house_search: bool = True):
        if do_exchange_bid_house_search:
            super().place_object(object_gid)
        assert self.selected_object['is_placed'] is False
        send_parsed_msg(
            self.common_info.message_to_send_queue,
            ExchangeBidHousePriceMessage(
                objectGID=object_gid,
            ),
        )
        self.selected_object['is_placed'] = True

        logger.info(
            f"sending ExchangeBidHousePriceMessage with objectGID : {object_gid}"
        )

    def close_selected_object(self):
        self.treated_objects_in_inventory.append(self.selected_object["object_gid"])
        super().close_selected_object()
        if self.is_playing_from_inventory_event.is_set():
            self.process_from_inventory()
        elif self.is_playing_update_event.is_set():
            self.process_update()

    def update_price_selected_object(self):
        assert self.selected_object is not None

        _object_to_update = self.objects_to_update.pop(0)

        results = self.get_price_and_quantity(
            self.selected_object["object_gid"],
            _object_to_update.quantity,
            self.selected_object["minimal_prices"],
        )
        logger.info(f"get price_and_quantity : {results}")
        if results is not None and results[1] != _object_to_update.objectPrice:
            quantity, price = results
            logger.info(
                f"send ExchangeObjectModifyPricedMessage gid : {self.selected_object['object_gid']}"
            )
            send_parsed_msg(
                self.common_info.message_to_send_queue,
                ExchangeObjectModifyPricedMessage(
                    objectUID=_object_to_update.objectUID,
                    price=price,
                    quantity=quantity,
                ),
            )
        else:
            logger.info(
                f"result is none, not updating object {self.selected_object['object_gid']}"
            )
            self.close_selected_object()
            # self.process_update()

    def sell_selected_object(self):
        assert self.selected_object is not None

        total_quantity = self.get_quantity_in_inventory(
            self.selected_object["object_gid"]
        )
        object_uid = next(
            _object.objectUID
            for _object in self.common_info.character.objects
            if _object.objectGID == self.selected_object["object_gid"]
        )
        results = self.get_price_and_quantity(
            self.selected_object["object_gid"],
            total_quantity,
            self.selected_object["minimal_prices"],
        )
        logger.info(f"get price_and_quantity : {results}")
        if results is not None:
            quantity, price = results
            send_parsed_msg(
                self.common_info.message_to_send_queue,
                ExchangeObjectMovePricedMessage(
                    objectUID=object_uid,
                    price=price,
                    quantity=quantity,
                ),
            )
            self.selected_object["is_placed"] = False
            return
        else:
            logger.info(
                f"result is none, cleaning inventory from object {self.selected_object['object_gid']}"
            )
            self.close_selected_object()
            self.process_from_inventory()

    def get_quantity_in_inventory(self, object_gid: int) -> int:
        return sum(
            _object.quantity
            for _object in self.common_info.character.objects
            if _object.objectGID == object_gid
        )

    def get_accepted_objects(self) -> list[int]:
        with sessionmaker(bind=self.engine)() as _session:
            if self.common_info.subscription_end_date <= datetime.now():
                accepted_gids = [
                    object_gid.id
                    for object_gid in _session.query(Item.id)
                    .join(TypeItem, Item.type_item_id == TypeItem.id)
                    .filter(
                        TypeItem.id.in_(self.accepted_objects_type), Item.level <= 60
                    )
                    .all()
                ]
            else:
                accepted_gids = [
                    object_gid.id
                    for object_gid in _session.query(Item.id)
                    .join(TypeItem, Item.type_item_id == TypeItem.id)
                    .filter(TypeItem.id.in_(self.accepted_objects_type))
                    .all()
                ]

            return accepted_gids

    def get_accepted_object_in_inventory(self) -> ObjectItem | None:
        assert self.common_info.character is not None
        accepted_objects_inventory = next(
            (
                object_
                for object_ in self.common_info.character.objects
                if object_.objectGID in self.accepted_objects_gid
                   and object_.objectGID not in self.treated_objects_in_inventory
            ),
            None,
        )
        logger.info(f"Get first accepted objects in inventory")
        return accepted_objects_inventory

    def get_price_and_quantity(
            self, object_gid: int, quantity: int, minimal_prices: list[int]
    ) -> Tuple[int, int] | None:
        if quantity == 0:
            return None

        quantity = int(f"1{str(0) * min((len(str(quantity)) - 1), 2)}")

        price = None
        for index, _price in enumerate(minimal_prices):
            if _price > 1:
                current_quantity = int(f"1{str(0) * index}")
                price = _price / current_quantity
                if current_quantity == quantity:
                    break
        if price is None:
            return None
        price = math.ceil(price * quantity)

        if not any(
                _object.quantity == quantity
                and _object.objectPrice == price
                and _object.objectGID == object_gid
                for _object in self.object_on_sale_info
        ):
            price -= 1

        if price <= 1:
            return None

        return quantity, price
