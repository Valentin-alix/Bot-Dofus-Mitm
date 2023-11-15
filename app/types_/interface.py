from __future__ import annotations

from dataclasses import dataclass, field
from queue import Queue
from threading import Event, Lock
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    # To avoid annoying circular import
    from app.modules.fm import Fm
    from app.modules.character import Character
    from app.modules.hdv.buying_hdv import BuyingHdv
    from app.modules.hdv.selling_hdv import SellingHdv
    from app.types_.parsed_message import ParsedMessage


class WithLock(TypedDict):
    lock: Lock


class OnSaleInfoWithLock(WithLock, TypedDict):
    number: int
    sum_price: int


class CharacterWithLock(WithLock, TypedDict):
    character: Character | None


class BuyingHdvWithLock(WithLock, TypedDict):
    buying_hdv: BuyingHdv | None


class SellingHdvWithLock(WithLock, TypedDict):
    selling_hdv: SellingHdv | None


class ServerIdWithLock(WithLock, TypedDict):
    server_id: int | None


class FmWithLock(WithLock, TypedDict):
    fm: Fm | None


class SelectedObject(TypedDict):
    quantity: int
    all_identical: bool
    object_gid: int
    object_uid: int
    minimal_prices: list[int]
    is_placed: bool


# Tread shared datas
@dataclass
class SnifferInfo:
    is_playing_event: Event = Event()
    parsed_message_queue: Queue[ParsedMessage] = Queue()


@dataclass
class FmInfo:
    is_playing_event: Event = Event()
    fm_with_lock: FmWithLock = field(default_factory=lambda: {"lock": Lock(), "fm": None})


@dataclass
class ScrapingInfo:
    is_playing_event: Event = Event()
    buying_hdv_with_lock: BuyingHdvWithLock = field(default_factory=lambda: {"lock": Lock(), "buying_hdv": None})


@dataclass
class SellingInfo:
    is_playing_event: Event = Event()
    on_sale_info_with_lock: OnSaleInfoWithLock = field(
        default_factory=lambda: {"lock": Lock(), "number": 0, "sum_price": 0})
    selling_hdv_with_lock: SellingHdvWithLock = field(default_factory=lambda: {"lock": Lock(), "selling_hdv": None})


@dataclass
class CommonInfo:
    is_closed_event: Event = Event()
    is_connected_event: Event = Event()
    message_to_send_queue: Queue[dict] = Queue()
    server_id_with_lock: ServerIdWithLock = field(default_factory=lambda: {"lock": Lock(), "server_id": None})
    character_with_lock: CharacterWithLock = field(default_factory=lambda: {"lock": Lock(), "character": None})


@dataclass
class BotInfo:
    common_info: CommonInfo = field(default_factory=CommonInfo)
    sniffer_info: SnifferInfo = field(default_factory=SnifferInfo)
    scraping_info: ScrapingInfo = field(default_factory=ScrapingInfo)
    fm_info: FmInfo = field(default_factory=FmInfo)
    selling_info: SellingInfo = field(default_factory=SellingInfo)
