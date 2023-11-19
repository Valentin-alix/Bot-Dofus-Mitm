from dataclasses import dataclass
from threading import Event

from app.modules.hdv.buying_hdv import BuyingHdv


@dataclass
class ScrapingInfo:
    buying_hdv: BuyingHdv | None = None
    is_playing_event: Event = Event()
