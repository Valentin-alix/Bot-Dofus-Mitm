from com.ankamagames.jerakine.logger.Logger import Logger
import base64
import sys
from typing import Any
from com.ankamagames.jerakine import JerakineConstants
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton
from com.ankamagames.jerakine.types.CustomSharedObject import CustomSharedObject
from com.ankamagames.jerakine.types.DataStoreType import DataStoreType
from com.ankamagames.jerakine.types.enums.DataStoreEnum import DataStoreEnum

logger = Logger(__name__)


class IExternalizable:
    pass


class Secure:
    pass


class StoreDataManager(metaclass=Singleton):
    def __init__(self) -> None:
        self._aData = dict()
        self._bStoreSequence: bool = False
        self._nCurrentSequenceNum: int = 0
        self._aStoreSequence: list = []
        self._aSharedObjectCache: dict = {}
        self._aRegisteredClassAlias: dict = {}
        self._bStoreSequence = False
        self._aRegisteredClassAlias = dict()
        self._self = None
        aClass = self.getData(JerakineConstants.DATASTORE_CLASS_ALIAS, "classAliasList")
        for s in aClass:
            className = base64.b64decode(s).decode()
            try:
                oClass = getattr(sys.modules[__package__], className)
                globals().update({aClass[s]: oClass})
            except Exception as e:
                # logger.warn("Impossible de trouver la classe " + className)
                self._aRegisteredClassAlias[className] = True
            self._aRegisteredClassAlias[className] = True

    def getSharedObject(self, sName: str) -> "CustomSharedObject":
        if sName in self._aSharedObjectCache:
            return self._aSharedObjectCache[sName]
        so = CustomSharedObject.getLocal(sName)
        self._aSharedObjectCache[sName] = so
        return so

    def getData(self, dataType: DataStoreType, sKey: str) -> Any:
        if dataType.persistant:
            if dataType.location == DataStoreEnum.LOCATION_LOCAL:
                so = self.getSharedObject(dataType.category)
                if so.data:
                    return so.data.get(sKey)
            elif dataType.location == DataStoreEnum.LOCATION_SERVER:
                return None
        if dataType.category in self._aData:
            return self._aData[dataType.category][sKey]
        return None

    def isComplexType(self, o) -> bool:
        if type(o) in [int, float, bool, list, str, None.__class__]:
            return False
        else:
            return True

    def registerClass(
        self, oInstance, deepClassScan: bool = False, keepClassInSo: bool = True
    ) -> None:
        if isinstance(oInstance, IExternalizable):
            raise Exception(
                "Can't store a customized IExternalizable in a shared object."
            )
        if isinstance(oInstance, Secure):
            raise Exception("Can't store a Secure class")
        if self.isComplexType(oInstance):
            className = oInstance.__class__.__name__
            sAlias = className.__hash__()
            if className not in self._aRegisteredClassAlias:
                return
            try:
                oClass = oInstance.__class__
                globals().update({sAlias: oClass})
                logger.warn("Register " + className)
            except Exception as e:
                self._aRegisteredClassAlias[className] = True
                logger.fatal(
                    "Impossible de trouver la classe "
                    + className
                    + " dans l'application domain courant"
                )
                return
            if keepClassInSo:
                aClassAlias = self.getSetData(
                    JerakineConstants.DATASTORE_CLASS_ALIAS, "classAliasList", []
                )
                aClassAlias[base64.encode(className)] = sAlias
                self.setData(
                    JerakineConstants.DATASTORE_CLASS_ALIAS,
                    "classAliasList",
                    aClassAlias,
                )
            self._aRegisteredClassAlias[className] = True
        if deepClassScan:
            if isinstance(oInstance, dict) or isinstance(oInstance, list):
                desc = oInstance
                if isinstance(oInstance, list[Any]):
                    tmp = oInstance.__class__.__name__
                    leftBracePos = tmp.find("[")
                    tmp = tmp[
                        leftBracePos
                        + 1 : str(reversed(tmp)).find("]")
                        - leftBracePos
                        - 1
                    ]
                    self.registerClass(oInstance.__class__(), True, keepClassInSo)
            else:
                desc = self.scanType(oInstance)
            for key in desc:
                if self.isComplexType(oInstance[key]):
                    self.registerClass(oInstance[key], True)
                if desc == oInstance:
                    break

    def setData(
        self, dataType: DataStoreType, sKey: str, oValue, deepClassScan: bool = False
    ) -> bool:
        so: CustomSharedObject = None
        if self._aData.get(dataType.category) == None:
            self._aData[dataType.category] = dict()
        self._aData[dataType.category][sKey] = oValue
        if dataType.persistant:
            if dataType.location == DataStoreEnum.LOCATION_LOCAL:
                self.registerClass(oValue, deepClassScan)
                so = self.getSharedObject(dataType.category)
                if not so.data:
                    so.data = {}
                so.data[sKey] = oValue
                if not self._bStoreSequence:
                    if not so.flush():
                        return False
                else:
                    self._aStoreSequence[dataType.category] = dataType
                return True
            if dataType.location == DataStoreEnum.LOCATION_SERVER:
                return False
        return True

    def getKeys(self, dataType: DataStoreType) -> list:
        so: CustomSharedObject = None
        key = None
        result: list = []
        if dataType.persistant:
            if dataType.location == DataStoreEnum.LOCATION_LOCAL:
                so = self.getSharedObject(dataType.category)
                data = so.datak
            if dataType.location == DataStoreEnum.LOCATION_SERVER:
                pass
        elif dataType.category in self._aData:
            data = self._aData[dataType.category]
        if data:
            for key in data:
                result.append(key)
        return result

    def getSetData(self, dataType: DataStoreType, sKey: str, oValue) -> Any:
        o = self.getData(dataType, sKey)
        if o != None:
            return o
        self.setData(dataType, sKey, oValue)
        return oValue

    def startStoreSequence(self) -> None:
        _bStoreSequence = True
        if not self._nCurrentSequenceNum:
            _aStoreSequence = []
        self._nCurrentSequenceNum += 1

    def stopStoreSequence(self) -> None:
        dt: DataStoreType = None
        s = None
        self._nCurrentSequenceNum -= 1
        _bStoreSequence = self._nCurrentSequenceNum != 0
        if _bStoreSequence:
            return
        for s in self._aStoreSequence:
            dt = self._aStoreSequence[s]
            if dt.location == DataStoreEnum.LOCATION_LOCAL:
                self.getSharedObject(dt.category).flush()
            elif DataStoreEnum.LOCATION_SERVER:
                break
        self._aStoreSequence = None

    def clear(self, dataType: DataStoreType) -> None:
        self._aData = []
        so: CustomSharedObject = self.getSharedObject(dataType.category)
        so.clear()

    def reset(self) -> None:
        s: CustomSharedObject = None
        for s in self._aSharedObjectCache:
            try:
                s.clear()
                s.close()
            except Exception as e:
                pass
        self._aSharedObjectCache = []

    def close(self, dataType: DataStoreType) -> None:
        if dataType.location == DataStoreEnum.LOCATION_LOCAL:
            self._aSharedObjectCache[dataType.category].close()
            del self._aSharedObjectCache[dataType.category]

    def isComplexTypeFromstr(self, name: str) -> bool:
        if name in ("int", "float", "str", "bool", "list", "float", None):
            return False
        else:
            return self._aRegisteredClassAlias[name]

    def scanType(self, obj) -> object:
        name: str = None
        desc: list[str] = DescribeTypeCache.getVariables(obj, False, True, True, True)
        result = {}
        for name in desc:
            if self.isComplexTypeFromstr(obj[name].__class__.__name__):
                result[name] = True
        return result
