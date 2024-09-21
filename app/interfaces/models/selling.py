from dataclasses import dataclass
from threading import Event

from app.modules.selling_sale_hotel import SellingSaleHotel


@dataclass
class SellingInfo:
    is_playing_from_inventory_event: Event = Event()
    is_playing_update_event: Event = Event()
    selling_hdv: SellingSaleHotel | None = None
