from dataclasses import dataclass
from threading import Event

from app.modules.hdv.selling_hdv import SellingHdv


@dataclass
class SellingInfo:
    is_playing_from_inventory_event: Event = Event()
    is_playing_update_event: Event = Event()
    selling_hdv: SellingHdv | None = None
