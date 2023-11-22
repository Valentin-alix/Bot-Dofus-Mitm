import logging
from threading import Thread, Event
from typing import TYPE_CHECKING

from app.database.models import get_engine
from app.gui.signals import AppSignals
from app.modules.hdv.hdv import Hdv
from app.network.utils import send_parsed_msg
from app.types_.dicts.common import EventValueChangeWithCallback
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseTypeMessage import (
    ExchangeBidHouseTypeMessage,
)

if TYPE_CHECKING:
    from app.types_.models.common import CommonInfo

logger = logging.getLogger(__name__)


class BuyingHdv(Hdv):
    def __init__(
            self,
            types: list[int],
            is_playing_event: Event,
            app_signals: AppSignals,
            common_info: 'CommonInfo',
    ) -> None:
        super().__init__(common_info)
        self.engine = get_engine()
        self.app_signals = app_signals
        self.is_playing_event = is_playing_event

        self.selected_type: int | None = None

        self.types_left = self.get_accepted_types(types)
        self.objects_left_in_type: list[dict] = []

        self.update_current_state()

        if self.is_playing_event.is_set():
            self.on_start(True)
        else:
            self.on_stop(True)

    def on_start(self, is_first: bool = False):
        if not is_first:
            self.process()
        check_event_change_thread = Thread(
            target=lambda: self.check_event_play(
                EventValueChangeWithCallback(
                    target_value=False,
                    event=self.is_playing_event,
                    callback=self.on_stop,
                )), daemon=True)
        check_event_change_thread.start()

    def on_stop(self, is_first: bool = False):
        if not is_first:
            if self.selected_object is not None:
                self.close_selected_object()
            if self.selected_type is not None:
                self.close_type()
        check_event_change_thread = Thread(
            target=lambda: self.check_event_play(
                EventValueChangeWithCallback(
                    target_value=True,
                    event=self.is_playing_event,
                    callback=self.on_start,
                )), daemon=True)
        check_event_change_thread.start()

    def __del__(self):
        self.app_signals.on_new_scraping_current_state.emit(
            {"category_remaining": 0, "object_remaining": 0}
        )

    def update_current_state(self):
        self.app_signals.on_new_scraping_current_state.emit(
            {
                "category_remaining": len(self.types_left),
                "object_remaining": len(self.objects_left_in_type),
            }
        )

    def process(self):
        if self.selected_object is not None:
            self.close_selected_object()
        elif len(self.objects_left_in_type) > 0:
            _object = self.objects_left_in_type.pop()
            self.place_object(_object["object_gid"])
        elif len(self.types_left) > 0:
            if self.selected_type is not None:
                self.close_type()
            else:
                self.place_type()
        else:
            logger.info("no object or type left to check prices")

        self.update_current_state()

    def place_type(self):
        assert len(self.types_left) > 0
        _type = self.types_left.pop()
        send_parsed_msg(
            self.common_info.message_to_send_queue,
            ExchangeBidHouseTypeMessage(
                follow=True,
                type=_type,
            ),
        )
        self.selected_type = _type
        logger.info(f"Sending check type {_type}")

    def close_type(self):
        assert self.selected_type is not None
        logger.info(f"Sending check type {self.selected_type} to close")
        send_parsed_msg(
            self.common_info.message_to_send_queue,
            ExchangeBidHouseTypeMessage(
                follow=False,
                type=self.selected_type,
            ),
        )
        self.selected_type = None
        if self.is_playing_event.is_set():
            self.process()
