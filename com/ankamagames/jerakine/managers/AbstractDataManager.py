from com.ankamagames.jerakine.logger.Logger import Logger
import math
from com.ankamagames.jerakine import JerakineConstants
from com.ankamagames.jerakine.managers.StoreDataManager import StoreDataManager
from com.ankamagames.jerakine.newCache.LruGarbageCollector import LruGarbageCollector
from com.ankamagames.jerakine.newCache.iCache import ICache
from com.ankamagames.jerakine.newCache.impl.cache import Cache
from com.ankamagames.jerakine.newCache.impl.infiniteCache import InfiniteCache
from com.ankamagames.jerakine.types.CustomSharedObject import CustomSharedObject

logger = Logger(__name__)


class AbstractDataManager(object):

    DATA_KEY: str = "data"

    def __init__(self) -> None:
        self._cacheKey: ICache = None
        self._cacheSO: Cache = None
        self._soPrefix: str = None

    def getObject(self, key: int) -> object:
        realKey: str = self._soPrefix + key
        if self._cacheKey.contains(realKey):
            return self._cacheKey.peek(realKey)
        chunkLength: int = StoreDataManager().getData(
            JerakineConstants.DATASTORE_FILES_INFO, self._soPrefix + "_chunkLength"
        )
        soName: str = self._soPrefix + str(math.floor(key / chunkLength))
        if self._cacheSO.contains(soName):
            foo = self._cacheSO.peek(soName)
            so: CustomSharedObject = self._cacheSO.peek(soName)
            v = so.data[self.DATA_KEY][key]
            self._cacheKey.store(realKey, v)
            return v
        so = CustomSharedObject.getLocal(soName)
        if not so or self.DATA_KEY not in so.data:
            return None
        self._cacheSO.store(soName, so)
        v = so.data[self.DATA_KEY][key]
        self._cacheKey.store(realKey, v)
        return v

    def getObjects(self) -> list:
        fileList: list = StoreDataManager().getData(
            JerakineConstants.DATASTORE_FILES_INFO, self._soPrefix + "_filelist"
        )
        if not fileList:
            return None
        data: list = list()
        for fileNum in fileList:
            soName = self._soPrefix + fileNum
            if self._cacheSO.contains(soName):
                so: CustomSharedObject = self._cacheSO.peek(soName)
                data += so.data[self.DATA_KEY]
            else:
                so = CustomSharedObject.getLocal(soName)
                if so and so.data.get(self.DATA_KEY):
                    self._cacheSO.store(soName, so)
                    data += so.data[self.DATA_KEY]
        return data

    def init(self, soCacheSize: int, keyCacheSize: int, soPrefix: str = "") -> None:
        if keyCacheSize == float("inf"):
            self._cacheKey = InfiniteCache()
        else:
            self._cacheKey = Cache.create(
                keyCacheSize, LruGarbageCollector(), self.__class__.__name__ + "_key"
            )
        self._cacheSO = Cache.create(
            soCacheSize, LruGarbageCollector(), self.__class__.__name__ + "_so"
        )
        self._soPrefix = soPrefix
