from typing import Any
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton
from com.ankamagames.jerakine.pools.Poolable import Poolable


class GenericPool(metaclass=Singleton):

    _pools: dict = dict()

    def __init__(self):
        super().__init__()

    def get(self, otype: object, *args) -> Any:
        if self._pools.get(otype) and len(self._pools[otype]):
            print("yes")
            return otype(*args, self._pools[otype].pop())
        return otype(*args)

    def free(self, target: Poolable) -> None:
        target.free()
        otype: object = target.__class__
        if otype not in self._pools:
            self._pools[otype] = list()
        self._pools[otype].append(target)


if __name__ == "__main__":

    class A(Poolable):
        def __init__(self, data):
            super().__init__()
            self.data = data

        def free(self):
            print("free")

    x = GenericPool().get(A, "aba")
    GenericPool().free(x)
    y = GenericPool().get(A, "test2")
    print(y.data)
    print(GenericPool()._pools)
