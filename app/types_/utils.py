from threading import Lock
from typing import TypedDict


class WithLock(TypedDict):
    lock: Lock
