import logging
from queue import Queue
from threading import Thread, Event
from time import sleep

from sqlalchemy.orm import sessionmaker

from app.database.models import TypeItem, get_engine
from app.gui.signals import AppSignals
from app.network.utils import send_parsed_msg
from app.types_.dicts.scraping import ScrapingCurrentState
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseSearchMessage import (
    ExchangeBidHouseSearchMessage,
)
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseTypeMessage import (
    ExchangeBidHouseTypeMessage,
)

logger = logging.getLogger(__name__)


class BuyingHdv:
    def __init__(self, categories: list[int], is_playing_event: Event, message_to_send_queue: Queue[dict],
                 scrapping_current_state: ScrapingCurrentState, app_signals: AppSignals) -> None:
        self.engine = get_engine()
        self.scrapping_current_state = scrapping_current_state
        self.app_signals = app_signals
        self.is_playing_event = is_playing_event
        self.message_to_send_queue = message_to_send_queue

        self.categories = self.get_consistent_categories(categories)
        self.types_object: list[dict] = []
        self.update_current_state()

        # TODO Use signal instead
        self.is_playing = self.is_playing_event.is_set()
        self.stop_timer = False
        check_event_play_thread = Thread(target=self.check_event_play, daemon=True)
        check_event_play_thread.start()

    def __del__(self):
        self.scrapping_current_state["category_remaining"] = 0
        self.scrapping_current_state["object_remaining"] = 0
        self.app_signals.on_new_scraping_current_state.emit(self.scrapping_current_state)

    def update_current_state(self):
        self.scrapping_current_state["category_remaining"] = len(self.categories)
        self.scrapping_current_state["object_remaining"] = len(self.types_object)
        self.app_signals.on_new_scraping_current_state.emit(self.scrapping_current_state)

    def check_event_play(self):
        """continuously check if event play has changed to true"""
        while not self.stop_timer:
            if (
                    not self.is_playing
                    and self.is_playing_event.is_set()
            ):
                logger.info("launching hdv bot after manual start")
                self.is_playing = True
                self.process()
            self.is_playing = self.is_playing_event.is_set()
            sleep(2)

    def get_consistent_categories(self, categories: list[int]) -> list[int]:
        """filter type category to be in database"""
        with sessionmaker(bind=self.engine)() as session:
            _consistent_types_category = [
                int(_type[0])
                for _type in (
                    session.query(TypeItem.id).filter(TypeItem.id.in_(categories)).all()
                )
            ]
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
                self.message_to_send_queue,
                ExchangeBidHouseTypeMessage(
                    follow=True,
                    type=category,
                ),
            )
            logger.info(f"Sending check category {category}")

    def send_get_prices(self, type_object):
        logger.info(f"Sending get prices {type_object.get('object_gid')}")
        send_parsed_msg(
            self.message_to_send_queue,
            ExchangeBidHouseSearchMessage(
                objectGID=type_object.get("object_gid"),
                follow=not type_object.get("is_opened"),
            ),
        )

    def process(self):
        if len(self.types_object) > 0:
            self.get_available_objects_gid()
        elif len(self.categories) > 0:
            self.send_get_category()
        self.update_current_state()
