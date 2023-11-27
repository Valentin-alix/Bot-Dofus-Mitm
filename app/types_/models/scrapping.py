from dataclasses import dataclass
from threading import Event

from app.modules.scrapping_sale_hotel import ScrappingSaleHotel


@dataclass
class ScrappingInfo:
    buying_hdv: ScrappingSaleHotel | None = None
    is_playing_event: Event = Event()
