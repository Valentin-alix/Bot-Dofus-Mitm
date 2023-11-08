from __future__ import annotations

from queue import Queue
from threading import Event, Lock
from typing import TYPE_CHECKING, TypedDict

from network.parsed_message.parsed_message import ParsedMessage

if TYPE_CHECKING:
    # To avoid annoying circular import
    from modules.character import Character
    from modules.hdv.buying_hdv import BuyingHdv
    from modules.hdv.selling_hdv import SellingHdv


class WithLock(TypedDict):
    lock: Lock


class CharacterWithLock(WithLock, TypedDict):
    character: Character | None


class BuyingHdvWithLock(WithLock, TypedDict):
    buying_hdv: BuyingHdv | None


class SellingHdvWithLock(WithLock, TypedDict):
    selling_hdv: SellingHdv | None


class ThreadsInfos(TypedDict):
    event_play_sniffer: Event
    event_play_hdv_scrapping: Event
    event_play_hdv_selling: Event
    event_close: Event
    event_connected: Event

    character_with_lock: CharacterWithLock
    buying_hdv_with_lock: BuyingHdvWithLock
    selling_hdv_with_lock: SellingHdvWithLock

    queue_msg_to_send: Queue[dict]
    queue_handler_message: Queue[ParsedMessage]
