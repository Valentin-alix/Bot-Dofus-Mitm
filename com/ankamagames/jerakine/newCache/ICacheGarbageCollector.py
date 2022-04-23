from abc import ABC
from typing import Any
from com.ankamagames.jerakine.newCache.impl.Cache import Cache


class ICacheGarbageCollector(ABC):
    @property
    def cache(self) -> Cache:
        pass

    @cache.setter
    def cache(param1: Cache) -> None:
        pass

    def used(param1: Any) -> None:
        pass

    def purge(param1: int) -> None:
        pass
