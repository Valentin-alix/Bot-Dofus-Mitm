from com.ankamagames.jerakine.logger.Logger import Logger
import math
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine import JerakineConstants
from com.ankamagames.jerakine.managers.StoreDataManager import StoreDataManager
from com.ankamagames.jerakine.newCache.ICache import ICache
from com.ankamagames.jerakine.newCache.impl.Cache import Cache
from com.ankamagames.jerakine.newCache.impl.InfiniteCache import InfiniteCache
from com.ankamagames.jerakine.types.CustomSharedObject import CustomSharedObject

logger = Logger(__name__)


class AbstractDataManager:
    DATA_KEY: str = "data"
    _cacheSO: ICache = None
    _cacheKey: ICache = None
    _soPrefix: str = ""

    @classmethod
    def getObject(cls, key: int) -> object:
        realKey: str = cls._soPrefix + str(key)
        if cls._cacheKey.contains(realKey):
            return cls._cacheKey.peek(realKey)
        chunkLength: int = StoreDataManager.getData(
            JerakineConstants.DATASTORE_FILES_INFO, cls._soPrefix + "_chunkLength"
        )
        soName: str = cls._soPrefix + str(math.floor(key / chunkLength))
        if cls._cacheSO.contains(soName):
            foo = cls._cacheSO.peek(soName)
            v = CustomSharedObject(cls._cacheSO.peek(soName)).data[cls.DATA_KEY][key]
            cls._cacheKey.store(realKey, v)
            return v
        so = CustomSharedObject.getLocal(soName)
        if not so or cls.DATA_KEY not in so.data:
            return None
        cls._cacheSO.store(soName, so)
        v = so.data[cls.DATA_KEY][key]
        cls._cacheKey.store(realKey, v)
        return v

    @classmethod
    def getObjects(cls) -> list:
        fileList: list = StoreDataManager.getData(
            JerakineConstants.DATASTORE_FILES_INFO, cls._soPrefix + "_filelist"
        )
        if not fileList:
            return None
        data: list = list()
        for fileNum in fileList:
            soName = cls._soPrefix + fileNum
            if cls._cacheSO.contains(soName):
                data = data.extend(
                    CustomSharedObject(cls._cacheSO.peek(soName)).data[cls.DATA_KEY]
                )
            else:
                so = CustomSharedObject.getLocal(soName)
                if so and cls.DATA_KEY in so.data:
                    cls._cacheSO.store(soName, so)
                    data = data.extend(so.data[cls.DATA_KEY])
        return data

    @classmethod
    def init(cls, soCacheSize: int, keyCacheSize: int, soPrefix: str = "") -> None:
        from com.ankamagames.jerakine.newCache.LruGarbageCollector import (
            LruGarbageCollector,
        )

        if keyCacheSize == float("inf"):
            cls._cacheKey = InfiniteCache()
        else:
            cls._cacheKey = Cache.create(
                keyCacheSize, LruGarbageCollector(), cls.__class__.__name__ + "_key"
            )
        cls._cacheSO = Cache.create(
            soCacheSize, LruGarbageCollector(), cls.__class__.__name__ + "_so"
        )
        cls._soPrefix = soPrefix
