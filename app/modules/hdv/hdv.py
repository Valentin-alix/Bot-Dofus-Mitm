from __future__ import annotations

import logging
from threading import Thread
from time import sleep
from typing import TYPE_CHECKING

from sqlalchemy.orm import sessionmaker

from app.database.models import get_engine, TypeItem
from app.gui.signals import AppSignals
from app.network.utils import send_parsed_msg
from app.types_.dicts.common import EventValueChangeWithCallback
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseSearchMessage import \
    ExchangeBidHouseSearchMessage

if TYPE_CHECKING:
    from app.types_.models.common import CommonInfo
    from app.types_.dicts.selling import SelectedObject

logger = logging.getLogger(__name__)


class Hdv:
    def __init__(self, common_info: CommonInfo, app_signals: AppSignals) -> None:
        self.common_info = common_info
        self.app_signals = app_signals

        self.engine = get_engine()
        self.event_change_thread: Thread | None = None

        # TODO Selected object can me multiple when buying hdv
        self.selected_object: SelectedObject | None = None
        self.stop_timer = False

    def __del__(self):
        self.clear()

    def clear(self):
        self.app_signals.on_leaving_hdv.emit()

    def check_event_change_thread(self, event_values_changes_with_callbacks: list[EventValueChangeWithCallback]):
        self.event_change_thread = Thread(target=lambda: self.check_event_change(event_values_changes_with_callbacks),
                                          daemon=True)
        self.event_change_thread.start()

    def check_event_change(self, event_values_changes_with_callbacks: list[EventValueChangeWithCallback]):
        """continuously check if event has changed to target value"""
        has_reached_target = False
        while not self.stop_timer and not has_reached_target:
            for event_value_change_with_callback in event_values_changes_with_callbacks:
                if event_value_change_with_callback['event'].is_set() is event_value_change_with_callback[
                    'target_value']:
                    logger.info("event value change detected")
                    logger.info(f"firing {event_value_change_with_callback['callback']}")
                    event_value_change_with_callback['callback']()
                    has_reached_target = True
                    break
            sleep(0.5)

    def place_object(self, object_gid: int):
        assert self.selected_object is None
        logger.info(f"Sending place object {object_gid}")
        send_parsed_msg(
            self.common_info.message_to_send_queue,
            ExchangeBidHouseSearchMessage(
                objectGID=object_gid,
                follow=True,
            ),
        )
        self.selected_object = {
            "object_gid": object_gid,
            "is_placed": False
        }

    def close_selected_object(self):
        assert self.selected_object is not None
        logger.info(
            f"sending ExchangeBidHouseSearchMessage with objectGID : {self.selected_object['object_gid']} to "
            f"close"
        )
        send_parsed_msg(
            self.common_info.message_to_send_queue,
            ExchangeBidHouseSearchMessage(
                follow=False,
                objectGID=self.selected_object["object_gid"],
            ),
        )
        self.selected_object = None

    def get_accepted_types(self, types_id: list[int]) -> list[int]:
        """filter type item to be in database"""
        with sessionmaker(bind=self.engine)() as session:
            accepted_types = [
                _type.id
                for _type in (
                    session.query(TypeItem.id)
                    .filter(TypeItem.id.in_(types_id))
                    .all()
                )
            ]
        return accepted_types
