import inspect
from types import FunctionType
from typing import Any
from collections.abc import Iterable
from com.ankamagames.dofus.misc.lists.GameDataList import GameDataList
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.GameDataField import GameDataField
from com.ankamagames.jerakine.data.GameDataFileAccessor import GameDataFileAccessor
from com.ankamagames.jerakine.data.I18nFileAccessor import I18nFileAccessor
from com.ankamagames.jerakine.enum.GameDataTypeEnum import GameDataTypeEnum
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.utils.misc.StringUtils import StringUtils

logger = Logger(__name__)


class GameDataQuery:
    def getQueryableFields(cls, target: object) -> list[str]:
        target = cls.checkPackage(target)
        return (
            GameDataFileAccessor()
            .getDataProcessor(target["MODULE"])
            .getQueryableField()
        )

    def union(cls, *idsVectors) -> list[int]:
        result: list[int] = list[int]()
        added: dict = dict()
        for idVector in idsVectors:
            if idVector != None:
                for id in idVector:
                    if not added.get(id):
                        result.append(id)
                        added[id] = True
        return result

    def intersection(cls, *idsVectors) -> list[int]:
        id: int = 0
        ind: int = 0
        newMatch: dict = None
        i: int = 0
        result: list[int] = list[int]()
        ids: list[int] = idsVectors[i]
        match: dict = dict()
        for ind in range(len(idsVectors[0])):
            match[idsVectors[0][ind]] = idsVectors[0][ind]
        for i in range(len(idsVectors)):
            newMatch = dict()
            for ind in range(len(idsVectors[i])):
                id = idsVectors[i][ind]
                if match[id]:
                    newMatch[id] = id
            match = newMatch
        for id in match:
            result.append(id)
        return result

    @classmethod
    def queryEquals(cls, target, fieldName: str, value) -> list[int]:
        target = cls.checkPackage(target)
        fieldName = cls.checkField(target, fieldName)
        if not fieldName:
            return list[int]()
        result = (
            GameDataFileAccessor()
            .getDataProcessor(getattr(target, "MODULE"))
            .queryEquals(fieldName, value)
        )
        if isinstance(value, Iterable):
            return cls.union(result)
        return result

    @classmethod
    def querystr(cls, target: object, fieldName: str, value: str) -> list[int]:
        target = cls.checkPackage(target)
        fieldName = cls.checkField(target, fieldName)
        if not fieldName:
            return list[int]()
        if not value:
            raise cls.ArgumentError("value arg cannot be None")
        return (
            GameDataFileAccessor()
            .getDataProcessor(target["MODULE"])
            .query(
                fieldName,
                cls.getMatchStringFct(StringUtils.noAccent(value).toLowerCase()),
            )
        )

    @classmethod
    def queryGreaterThan(cls, target: object, fieldName: str, value) -> list[int]:
        target = cls.checkPackage(target)
        fieldName = cls.checkField(target, fieldName)
        if not fieldName:
            return list[int]()
        return (
            GameDataFileAccessor()
            .getDataProcessor(target["MODULE"])
            .query(fieldName, cls.getGreaterThanFct(value))
        )

    @classmethod
    def querySmallerThan(cls, target: object, fieldName: str, value) -> list[int]:
        target = cls.checkPackage(target)
        fieldName = cls.checkField(target, fieldName)
        if not fieldName:
            return list[int]()
        return (
            GameDataFileAccessor()
            .getDataProcessor(target["MODULE"])
            .query(fieldName, cls.getSmallerThanFct(value))
        )

    @classmethod
    def returnInstance(cls, target: object, ids: list[int]) -> list[object]:
        instance = None
        target = cls.checkPackage(target)
        result: list[object] = list[object]()
        module: str = target["MODULE"]
        for i in range(len(ids)):
            instance = GameData.getObject(module, ids[i])
            if instance != None:
                result.append(instance)
        return result

    @classmethod
    def sort(
        cls, target: object, ids: list[int], fieldNames, ascending=True
    ) -> list[int]:
        cleanedFieldNames: list[str] = None
        i: int = 0
        field: str = None
        target = cls.checkPackage(target)
        if not isinstance(fieldNames, str):
            cleanedFieldNames = list[str]()
            for i in range(len(fieldNames)):
                field = cls.checkField(target, fieldNames[i])
                if field:
                    cleanedFieldNames.append(field)
            fieldNames = cleanedFieldNames
        else:
            fieldNames = cls.checkField(target, fieldNames)
        if not fieldNames or len(fieldNames) == 0:
            return list[int]()
        return (
            GameDataFileAccessor()
            .getDataProcessor(target["MODULE"])
            .sort(fieldNames, ids, ascending)
        )

    @classmethod
    def sortI18n(cls, datas, fields, ascending) -> Any:
        datas.sort(cls.getSortFunction(datas, fields, ascending))
        return datas

    @classmethod
    def getSortFunction(cls, datas, fieldNames, ascending) -> FunctionType:
        sortWay: list[float] = None
        indexes: list[dict] = None
        maxFieldIndex: int = 0
        fieldName: str = None
        fieldIndex: dict = None
        data = None
        if isinstance(fieldNames, str):
            fieldNames = [fieldNames]
        if ascending is bool:
            ascending = [ascending]
        sortWay = list[float]()
        indexes = list[dict]()
        for i in range(len(fieldNames)):
            fieldName = fieldNames[i]
            fieldIndex = dict()
            for data in datas:
                fieldIndex[data[fieldName]] = I18nFileAccessor().getOrderIndex(
                    data[fieldName]
                )
            if len(ascending) < len(fieldNames):
                ascending.append(True)
            sortWay.append(1 if not ascending[i] else -1)
            indexes.append(fieldIndex)
        maxFieldIndex = len(fieldNames)

        def function(t1, t2) -> float:
            for fieldIndex in range(maxFieldIndex):
                if (
                    indexes[fieldIndex][t1[fieldNames[fieldIndex]]]
                    < indexes[fieldIndex][t2[fieldNames[fieldIndex]]]
                ):
                    return -sortWay[fieldIndex]
                if (
                    indexes[fieldIndex][t1[fieldNames[fieldIndex]]]
                    > indexes[fieldIndex][t2[fieldNames[fieldIndex]]]
                ):
                    return sortWay[fieldIndex]
            return 0

        return function

    @classmethod
    def getMatchStringFct(cls, pattern: str) -> FunctionType:
        return (
            lambda s: StringUtils.noAccent(str).toLowerCase().find(pattern) != -1
            if s
            else False
        )

    @classmethod
    def getGreaterThanFct(cls, cmpValue) -> FunctionType:
        return lambda v: v > cmpValue

    @classmethod
    def getSmallerThanFct(cls, cmpValue) -> FunctionType:
        return lambda v: v < cmpValue

    @classmethod
    def checkField(cls, target: object, name: str) -> str:
        module = getattr(target, "MODULE")
        fields = GameDataFileAccessor().getDataProcessor(module).getQueryableField()
        if name not in fields:
            fieldType = (
                GameDataFileAccessor()
                .getDataProcessor(module)
                .getFieldType(name + "Id")
            )
            if (
                name + "Id" not in fields
                or GameDataTypeEnum(fieldType) != GameDataTypeEnum.I18N
            ):
                logger.error("Field " + name + " not found in " + target.__name__)
                return None
            name += "Id"
        return name

    @classmethod
    def checkPackage(cls, target) -> object:
        module: str = inspect.getmodule(target)
        moduleName = module.__name__
        if "d2data" in moduleName:
            className = target.__name__
            for gameDataobject in GameDataList.CLASSES:
                gameDataobjectName = gameDataobject.__name__
                if gameDataobjectName == className:
                    return GameDataField.getobjectByName(gameDataobjectName)
        elif moduleName.find("com.ankamagames.dofus.datacenter") != 0:
            raise Exception(
                target.__name__ + " is queryable (note found in datacenter package)."
            )
        return target
