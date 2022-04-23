# utf-8
import io
from com.ankamagames.jerakine.logger.Logger import Logger
import os
from com.ankamagames.dofus import Constants as Constants
import pyamf

logger = Logger(__name__)


class CustomSharedObjectFileFormatError(Exception):
    pass


class CustomSharedObject:

    DATAFILE_EXTENSION = "dat"
    COMMON_FOLDER = Constants.DOFUS_LOCAL_DATA_STORE
    directory = "Dofus"
    useDefaultDirectory = False
    clearedCacheAndRebooting = False
    throwException = True
    _cache = dict[str, "CustomSharedObject"]()
    data = None

    def __init__(self):
        self.data = None
        self.objectEncoding: int = None
        self._name: str = None
        self._fileStream: io.BytesIO = None
        self._file: str = None

    @classmethod
    def getLocal(cls, name: str) -> "CustomSharedObject":
        if cls._cache.get(name):
            return cls._cache[name]
        if not cls.COMMON_FOLDER:
            cls.COMMON_FOLDER = cls.getCustomSharedObjectDirectory()
        cso: CustomSharedObject = CustomSharedObject()
        cso._name = name
        cso.getDataFromFile()
        cls._cache[name] = cso
        return cso

    @classmethod
    def getCustomSharedObjectDirectory(cls) -> str:
        return cls.COMMON_FOLDER

    @classmethod
    def closeAll(cls) -> None:
        for cso in cls._cache:
            if cso:
                cso.close()

    @classmethod
    def resetCache(cls) -> None:
        cls._cache = []

    @classmethod
    def clearCache(cls, name: str) -> None:
        del cls._cache[name]

    def flush(self) -> None:
        if self.clearedCacheAndRebooting:
            return
        self.writeData(self.data)

    def clear(self) -> None:
        self.data = object()
        self.writeData(self.data)

    def close(self) -> None:
        if self._fileStream:
            self._fileStream.close()

    def writeData(self, data) -> bool:
        try:
            self._fileStream = open(self._file, "wb")
            amfEncoded = pyamf.encode(data)
            self._fileStream.write(amfEncoded.read())
            self._fileStream.close()
        except Exception as e:
            if self._fileStream:
                self._fileStream.close()
            logger.error(f"Unable to write file : {self._file}", exc_info=True)
            return False
        return True

    def getDataFromFile(self) -> None:
        if not self._file:
            self._file = os.path.join(
                self.COMMON_FOLDER, self._name + "." + self.DATAFILE_EXTENSION
            )
        logger.debug("Loading file : " + self._file)
        if os.path.exists(self._file):
            try:
                with open(self._file, "rb") as fp:
                    self._fileStream = fp
                    c = pyamf.decode(fp.read())
                    c = list(c)
                    if c:
                        self.data = c[0]
                    else:
                        self.data = {}
            except Exception as e:
                if self._fileStream:
                    self._fileStream.close()
                logger.error("Impossible d'ouvrir le fichier " + self._file)
                if self.throwException:
                    raise CustomSharedObjectFileFormatError(
                        "Malformated file : " + self._file
                    )
        if not self.data:
            self.data = dict()
