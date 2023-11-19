from dataclasses import dataclass, field
from threading import Event

from app.modules.hdv.buying_hdv import BuyingHdv
from app.types_.dicts.scraping import ScrapingCurrentState


@dataclass
class ScrapingInfo:
    current_state: ScrapingCurrentState = field(
        default_factory=lambda: {"category_remaining": 0, "object_remaining": 0})
    buying_hdv: BuyingHdv | None = None
    is_playing_event: Event = Event()
