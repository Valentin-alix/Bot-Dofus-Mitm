from dataclasses import dataclass
from datetime import datetime
import logging
from threading import Timer
from copy import deepcopy
from sqlalchemy.orm import sessionmaker
from database.models import Object, Price, TypeObject, get_engine
from types_ import (
    ExchangeBidHouseSearchMessage,
    ExchangeTypesExchangerDescriptionForUserMessage,
    ExchangeTypesItemsExchangerDescriptionForUserMessage,
    SellerBuyerDescriptor,
)
from types_.interface import ExchangeBidHouseTypeMessage, ThreadsInfos

logger = logging.getLogger(__name__)


class Hdv:
    def __init__(
        self,
        seller_buyer_descriptor: SellerBuyerDescriptor,
        threads_infos: ThreadsInfos,
    ) -> None:
        self.categories = seller_buyer_descriptor.get("types")
        self.engine = get_engine()
        session = sessionmaker(bind=self.engine)()

        # Get normal categories
        _types = [
            int(_type[0])
            for _type in (
                session.query(TypeObject.type_id)
                .filter(TypeObject.type_id.in_(self.categories))
                .all()
            )
        ]
        self.categories = [
            category for category in self.categories if category in _types
        ]

        self.threads_infos = threads_infos
        self.types_object: list[dict] = []

        self.is_playing = self.threads_infos.get("event_play_hdv").is_set()
        if self.is_playing:
            self.process()
        Timer(1, self.check_event_play).start()

    def check_event_play(self):
        if not self.threads_infos.get("event_close").is_set():
            if (
                not self.is_playing
                and self.threads_infos.get("event_play_hdv").is_set()
            ):
                logger.info("launching hdv bot after init")
                self.process()
            self.is_playing = self.threads_infos.get("event_play_hdv").is_set()
            Timer(1, self.check_event_play).start()

    def get_available_objects_gid(self):
        if len(self.types_object) > 0:
            type_object = self.types_object[-1]
            if type_object.get("is_opened"):
                # close prices panel and remove object from list
                self.send_get_prices_gid(self.types_object.pop())
                self.update_remaining_hdv()
            else:
                # open prices panel
                self.send_get_prices_gid(type_object)
                type_object["is_opened"] = True

    def send_check_category(self):
        if len(self.categories) > 0:
            category = self.categories.pop()
            exchange_bid_house_type_message_exchange_bid_house_type_message = vars(
                ExchangeBidHouseTypeMessage(
                    __type__="ExchangeBidHouseTypeMessage",
                    from_client=True,
                    follow=True,
                    type=category,
                )
            )
            logger.info(f"Sending check category {category}")
            self.threads_infos["queue_msg_to_send"].put(
                exchange_bid_house_type_message_exchange_bid_house_type_message
            )
            self.update_remaining_hdv()

    def send_get_prices_gid(self, type_object):
        logger.info(f"Sending get prices {type_object.get('object_gid')}")
        exchange_bid_house_search_message = ExchangeBidHouseSearchMessage(
            __type__="ExchangeBidHouseSearchMessage",
            from_client=True,
            objectGID=type_object.get("object_gid"),
            follow=not type_object.get("is_opened"),
        )
        self.threads_infos["queue_msg_to_send"].put(
            vars(exchange_bid_house_search_message)
        )

    def on_received_checked_category(
        self, parsed_message: ExchangeTypesExchangerDescriptionForUserMessage
    ):
        for type_description in parsed_message.typeDescription:
            self.types_object.append(
                {"object_gid": type_description, "is_opened": False}
            )

        self.process()

    def on_receive_get_prices_gid(
        self, parsed_message: ExchangeTypesItemsExchangerDescriptionForUserMessage
    ):
        session = sessionmaker(bind=self.engine)()
        if len(parsed_message.itemTypeDescriptions) == 1:
            # Saving prices in database
            _object = (
                session.query(Object)
                .filter_by(object_gid=parsed_message.objectGID)
                .first()
            )
            if _object is not None:
                prices_values = ",".join(
                    str(price)
                    for price in parsed_message.itemTypeDescriptions[0].get("prices")
                )
                price = Price(
                    creation_date=datetime.now(),
                    object_id=_object.id,
                    list_prices=prices_values,
                )
                session.add(price)
                session.commit()

                session.close()

        self.process()

    def update_remaining_hdv(self):
        self.threads_infos["queue_current_hdv"].put(
            {
                "objects_remaining": len(self.types_object),
                "categories_remaining": len(self.categories),
            },
        )

    def process(self):
        if len(self.types_object) > 0:
            self.get_available_objects_gid()
        elif len(self.categories) > 0:
            self.send_check_category()
