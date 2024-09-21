from __future__ import annotations

from threading import Event
from typing import TypedDict, Callable


class EventValueChangeWithCallback(TypedDict):
    target_value: bool
    event: Event
    callback: Callable
