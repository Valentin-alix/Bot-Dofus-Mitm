from com.ankamagames.jerakine import JerakineConstants
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton
import com.ankamagames.jerakine.pools.Pool as pool


logger = Logger(__name__)


class PoolsManager(metaclass=Singleton):

    _loadersPool: pool.Pool

    _urlLoadersPool: pool.Pool

    _rectanglePool: pool.Pool

    _pointPool: pool.Pool

    _soundPool: pool.Pool

    _linkedListNodePool: pool.Pool

    _jsonEncoderPool: pool.Pool

    _jsonDecoderPool: pool.Pool

    _linkedListNodePool = None

    def getLinkedListNodePool(self) -> pool.Pool:
        if not self._linkedListNodePool:
            from com.ankamagames.jerakine.pools.PoolableLinkedListNode import (
                PoolableLinkedListNode,
            )

            self._linkedListNodePool = pool.Pool(
                pooledClass=PoolableLinkedListNode,
                initialSize=JerakineConstants.LINKED_LIST_NODE_POOL_INITIAL_SIZE,
                growSize=JerakineConstants.LINKED_LIST_NODE_POOL_GROW_SIZE,
                warnLimit=JerakineConstants.LINKED_LIST_NODE_POOL_WARN_LIMIT,
            )
        return self._linkedListNodePool
