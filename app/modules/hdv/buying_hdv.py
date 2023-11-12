import logging
from threading import Thread
from time import sleep

from sqlalchemy.orm import sessionmaker

from app.database.models import TypeItem, get_engine
from app.network.utils import send_parsed_msg
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseSearchMessage import (
    ExchangeBidHouseSearchMessage,
)
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseTypeMessage import (
    ExchangeBidHouseTypeMessage,
)
from app.types_.interface import BotInfo

logger = logging.getLogger(__name__)


class BuyingHdv:
    def __init__(self, categories: list[int], bot_info: BotInfo) -> None:
        self.engine = get_engine()
        self.categories = self.get_consistent_categories(categories)
        self.types_object: list[dict] = []

        self.bot_info = bot_info

        self.is_playing = self.bot_info.scraping_info.is_playing_event.is_set()
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
                    and self.bot_info.scraping_info.is_playing_event.is_set()
            ):
                logger.info("launching hdv bot after manual start")
                self.is_playing = True
                self.process()
            self.is_playing = self.bot_info.scraping_info.is_playing_event.is_set()
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
            send_parsed_msg(
                self.bot_info,
                ExchangeBidHouseTypeMessage(
                    follow=True,
                    type=category,
                ),
                from_client=True,
            )
            logger.info(f"Sending check category {category}")

    def send_get_prices(self, type_object):
        logger.info(f"Sending get prices {type_object.get('object_gid')}")
        send_parsed_msg(
            self.bot_info,
            ExchangeBidHouseSearchMessage(
                objectGID=type_object.get("object_gid"),
                follow=not type_object.get("is_opened"),
            ),
            True,
        )

    def process(self):
        if len(self.types_object) > 0:
            self.get_available_objects_gid()
        elif len(self.categories) > 0:
            self.send_get_category()
