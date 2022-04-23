from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.pools.Poolable import Poolable
from com.ankamagames.jerakine.pools.PoolableLinkedListNode import PoolableLinkedListNode
from mx.utils.LinkedList import LinkedList
from mx.utils.LinkedListNode import LinkedListNode

logger = Logger(__name__)


class Pool:

    _pooledClass: object
    _pool: LinkedList
    _growSize: int
    _warnLimit: int
    _totalSize: int

    def __init__(
        self, pooledClass: object, initialSize: int, growSize: int, warnLimit: int = 0
    ):
        super().__init__()
        self._pooledClass = pooledClass
        if self._pooledClass is PoolableLinkedListNode:
            self._pool = LinkedList()
        else:
            import com.ankamagames.jerakine.pools.PoolLinkedList as poolLinkedList

            self._pool = poolLinkedList.PoolLinkedList()
        self._growSize = growSize
        self._warnLimit = warnLimit
        for _ in range(initialSize):
            self._pool.unshift(self._pooledClass())
        self._totalSize = initialSize

    @property
    def pooledClass(self) -> object:
        return self._pooledClass

    @property
    def poolList(self) -> LinkedList:
        return self._pool

    @property
    def growSize(self) -> int:
        return self._growSize

    @property
    def warnLimit(self) -> int:
        return self._warnLimit

    def checkOut(self) -> Poolable:
        if self._pool.length == 0:
            for i in range(self._growSize):
                self._pool.append(self._pooledClass())
            self._totalSize += self._growSize
            if self._warnLimit > 0 and self._totalSize > self._warnLimit:
                # logger.warn(f"Pool of {self._pooledClass.__name__} size beyond the warning limit. Size: {self._totalSize} , limit: {self._warnLimit}.")
                pass
        node: LinkedListNode = self._pool.shift()
        if self._pooledClass is PoolableLinkedListNode:
            o = node
        else:
            o = node.value
            from com.ankamagames.jerakine.pools.PoolsManager import PoolsManager

            PoolsManager().getLinkedListNodePool().checkIn(node)
        return o

    def checkIn(self, freedobject: Poolable) -> None:
        if not freedobject:
            return
        freedobject.free()
        self._pool.append(freedobject)
