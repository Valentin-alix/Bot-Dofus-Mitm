from dataclasses import dataclass, field
from threading import Event

from app.modules.hdv.selling_hdv import SellingHdv
from app.types_.dicts.selling import OnSaleInfoWithLock


@dataclass
class SellingInfo:
    is_playing_from_inventory_event: Event = Event()
    is_playing_update_event: Event = Event()
    on_sale_info_with_lock: OnSaleInfoWithLock = field(
        default_factory=lambda: {"number": 0, "sum_price": 0}
    )
    selling_hdv: SellingHdv | None = None
