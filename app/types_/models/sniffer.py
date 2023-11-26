from dataclasses import dataclass
from threading import Event


@dataclass
class SnifferInfo:
    is_playing_event: Event = Event()
