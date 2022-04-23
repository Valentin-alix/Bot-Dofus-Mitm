from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from com.ankamagames.jerakine.newCache.ICacheGarbageCollector import (
        ICacheGarbageCollector,
    )
from com.ankamagames.jerakine.newCache.ICache import ICache
from com.ankamagames.jerakine.newCache.impl.InfiniteCache import InfiniteCache


class Cache(InfiniteCache, ICache):

    _namedCacheIndex: list = list()
    _bounds: int
    _gc: "ICacheGarbageCollector"
    _name: str

    def __init__(self, bounds: int, gc: "ICacheGarbageCollector"):
        super().__init__()
        self._bounds = bounds
        self._gc = gc
        self._gc.cache = self

    def create(self, bounds: int, gc: "ICacheGarbageCollector", name: str) -> "Cache":
        cache: Cache = None
        if name and self._namedCacheIndex[name]:
            return self._namedCacheIndex[name]
        cache = Cache(bounds, gc)
        if name:
            self._namedCacheIndex[name] = cache
            cache._name = name
        return cache

    def destroy(self) -> None:
        if self._name:
            del self._namedCacheIndex[self._name]
        super().destroy()

    def extract(self, ref) -> Any:
        self._gc.used(ref)
        return super().extract(ref)

    def peek(self, ref) -> Any:
        self._gc.used(ref)
        return super().peek(ref)

    def store(self, ref, obj) -> bool:
        bb: int = 0
        if self._bounds and self._size + 1 > self._bounds:
            bb = self._bounds * 0.7 + 1 >> 0
            self._gc.purge(bb)
        super().store(ref, obj)
        self._gc.used(ref)
        return True
