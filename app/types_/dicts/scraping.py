from typing import TypedDict

from app.types_.utils import WithLock


class ScrapingCurrentState(WithLock, TypedDict):
    category_remaining: int
    object_remaining: int
