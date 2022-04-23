from typing import TYPE_CHECKING
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.enum.GameDataTypeEnum import GameDataTypeEnum
from com.ankamagames.jerakine.data.BinaryStream import BinaryStream

if TYPE_CHECKING:
    from ankamagames.jerakine.data.ModuleReader import ModuleReader
logger = Logger(__name__)


class GameDataField:

    NULL_IDENTIFIER: int = -1431655766
    _classesByName = dict()

    def __init__(self, name: str, moduleReader: "ModuleReader"):
        self.name = name
        self._innerReadMethods = list()
        self._innerTypeNames = list()
        self.moduleReader = moduleReader

    def readType(self, stream: BinaryStream):
        typeId = stream.readInt()
        self.readData = self.getReadMethod(typeId, stream)

    def getReadMethod(self, typeId, stream: BinaryStream):

        if typeId == GameDataTypeEnum.INT:
            return self.readInteger

        elif typeId == GameDataTypeEnum.BOOLEAN:
            return self.readbool

        elif typeId == GameDataTypeEnum.STRING:
            return self.readstr

        elif typeId == GameDataTypeEnum.NUMBER:
            return self.readNumber

        elif typeId == GameDataTypeEnum.I18N:
            return self.readI18n

        elif typeId == GameDataTypeEnum.UINT:
            return self.readUnsignedInteger

        elif typeId == GameDataTypeEnum.VECTOR:
            self._innerTypeNames.append(stream.readUTF())
            self._innerReadMethods.insert(
                0, self.getReadMethod(stream.readInt(), stream)
            )
            return self.readVector

        else:
            if typeId > 0:
                return self.readobject
            raise Exception("Unknown type '" + typeId + "'.")

    def readInteger(self, stream: BinaryStream, innerIndex=0):
        return stream.readInt()

    def readbool(self, stream: BinaryStream, innerIndex=0):
        return stream.readbool()

    def readstr(self, stream: BinaryStream, innerIndex=0):
        result = stream.readUTF()
        if result == "null":
            result = None
        return result

    def readNumber(self, stream: BinaryStream, innerIndex=0):
        return stream.readDouble()

    def readI18n(self, stream: BinaryStream, innerIndex=0):
        return stream.readInt()

    def readUnsignedInteger(self, stream: BinaryStream, innerIndex=0):
        return stream.readInt()

    def readVector(self, stream: BinaryStream, innerIndex=0):
        vector_size = stream.readInt()
        vector = list()
        for i in range(vector_size):
            vector.append(self._innerReadMethods[innerIndex](stream, innerIndex + 1))
            i += 1
        return vector

    def readobject(self, stream: BinaryStream, innerIndex=0):
        classIdentifier = stream.readInt()
        if classIdentifier == self.NULL_IDENTIFIER:
            return None
        classDefinition = self.moduleReader.getClassDefinition(classIdentifier)
        return classDefinition.getInstance(stream)

    @classmethod
    def getobjectByName(cls, className: str) -> object:
        c: object = cls._classesByName.get(className)
        if c is None:
            c = globals()[className]
            cls._classesByName[className] = c
        return c
