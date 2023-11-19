from dataclasses import dataclass
from threading import Event

from app.modules.fm import Fm


@dataclass
class FmInfo:
    is_playing_event: Event = Event()
    fm: Fm | None = None
