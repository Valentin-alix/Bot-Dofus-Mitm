import logging
from threading import Thread
from time import sleep

from database.models import TypeItem, get_engine
from network.parsed_message.parsed_message_client.exchanges.exchange_bid_house_search_message import (
    ExchangeBidHouseSearchMessage,
)
from network.parsed_message.parsed_message_client.exchanges.exchange_bid_house_type_message import (
    ExchangeBidHouseTypeMessage,
)
from sqlalchemy.orm import sessionmaker

from types_.interface import ThreadsInfos

logger = logging.getLogger(__name__)


class BuyingHdv:
    def __init__(self, categories: list[int], threads_infos: ThreadsInfos) -> None:
        self.engine = get_engine()
        self.categories = self.get_consistent_categories(categories)
        self.types_object: list[dict] = []

        self.threads_infos = threads_infos

        self.is_playing = self.threads_infos.get("event_play_hdv_scrapping").is_set()
        self.stop_timer = False

        check_event_play_thread = Thread(target=self.check_event_play, daemon=True)
        check_event_play_thread.start()

    def check_event_play(self):
        """continuously check if event play has changed to true"""
        while (
            not self.threads_infos.get("event_close").is_set() and not self.stop_timer
        ):
            if (
                not self.is_playing
                and self.threads_infos.get("event_play_hdv_scrapping").is_set()
            ):
                logger.info("launching hdv bot after manual start")
                self.is_playing = True
                self.process()
            self.is_playing = self.threads_infos.get(
                "event_play_hdv_scrapping"
            ).is_set()
            sleep(2)

    def get_consistent_categories(self, categories: list[int]) -> list[int]:
        """filter type category to be in database"""
        session = sessionmaker(bind=self.engine)()
        _consistent_types_category = [
            int(_type[0])
            for _type in (
                session.query(TypeItem.id).filter(TypeItem.id.in_(categories)).all()
            )
        ]
        session.close()
        return _consistent_types_category

    def get_available_objects_gid(self):
        if len(self.types_object) > 0:
            type_object = self.types_object[-1]
            if type_object.get("is_opened"):
                # close prices panel and remove object from list
                self.send_get_prices(self.types_object.pop())
            else:
                # open prices panel
                self.send_get_prices(type_object)
                type_object["is_opened"] = True

    def send_get_category(self):
        if len(self.categories) > 0:
            category = self.categories.pop()
            exchange_bid_house_type_message_exchange_bid_house_type_message = (
                ExchangeBidHouseTypeMessage(
                    __type__="ExchangeBidHouseTypeMessage",
                    from_client=True,
                    follow=True,
                    type=category,
                )
            )
            exchange_bid_house_type_message_exchange_bid_house_type_message.send(
                self.threads_infos
            )
            logger.info(f"Sending check category {category}")

    def send_get_prices(self, type_object):
        logger.info(f"Sending get prices {type_object.get('object_gid')}")
        exchange_bid_house_search_message = ExchangeBidHouseSearchMessage(
            __type__="ExchangeBidHouseSearchMessage",
            from_client=True,
            objectGID=type_object.get("object_gid"),
            follow=not type_object.get("is_opened"),
        )
        exchange_bid_house_search_message.send(self.threads_infos)

    def process(self):
        if len(self.types_object) > 0:
            self.get_available_objects_gid()
        elif len(self.categories) > 0:
            self.send_get_category()
