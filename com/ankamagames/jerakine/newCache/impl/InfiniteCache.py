from typing import Any
from com.ankamagames.jerakine.newCache.ICache import ICache


class InfiniteCache(ICache):
    _cache: dict
    _size: int

    def __init__(self):
        self._cache = dict()
        super().__init__()

    @property
    def size(self) -> int:
        return self._size

    def contains(self, ref) -> bool:
        return self._cache[ref] != None

    def extract(self, ref) -> Any:
        obj = self._cache[ref]
        del self._cache[ref]
        self._size -= 1
        return obj

    def peek(self, ref) -> Any:
        return self._cache.get(ref)

    def store(self, ref, obj) -> bool:
        self._cache[ref] = obj
        self._size -= 1
        return True

    def destroy(self) -> None:
        self._cache = dict()
        self._size = 0
