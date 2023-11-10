from __future__ import annotations

from queue import Queue
from threading import Event, Lock
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    # To avoid annoying circular import
    from app.modules.character import Character
    from app.modules.hdv.buying_hdv import BuyingHdv
    from app.modules.hdv.selling_hdv import SellingHdv
    from app.types_.parsed_message import ParsedMessage


class WithLock(TypedDict):
    lock: Lock


class CharacterWithLock(WithLock, TypedDict):
    character: Character | None


class BuyingHdvWithLock(WithLock, TypedDict):
    buying_hdv: BuyingHdv | None


class SellingHdvWithLock(WithLock, TypedDict):
    selling_hdv: SellingHdv | None


class ServerIdWithLock(WithLock, TypedDict):
    server_id: int | None


class SelectedObject(TypedDict):
    all_identical: bool
    generic_id: int
    minimal_prices: list[int]
    is_placed: bool
    name: str | None


class ThreadsInfos(TypedDict):
    event_play_sniffer: Event
    event_play_hdv_scrapping: Event
    event_play_hdv_selling: Event
    event_close: Event
    event_connected: Event

    character_with_lock: CharacterWithLock
    buying_hdv_with_lock: BuyingHdvWithLock
    selling_hdv_with_lock: SellingHdvWithLock
    server_id_with_lock: ServerIdWithLock

    queue_for_sale_object: Queue[SelectedObject]
    queue_msg_to_send: Queue[dict]
    queue_handler_message: Queue[ParsedMessage]
