from collections import OrderedDict
from com.ankamagames.jerakine.logger.Logger import Logger
from typing import Any
from com.ankamagames.jerakine.data.GameDataProcess import GameDataProcess
from com.hurlan.crypto.Signature import Signature
from com.ankamagames.jerakine.data.BinaryStream import BinaryStream
from com.ankamagames.jerakine.data.GameDataClassDefinition import (
    GameDataClassDefinition,
)

logger = Logger(__name__)


class InvalidD2OFile(Exception):
    pass


class ModuleReader:
    def __init__(self, stream: BinaryStream) -> None:
        """Init the class with the informations about files in the D2O"""
        if not isinstance(stream, BinaryStream):
            stream = BinaryStream(stream, True)
        # Attributes
        self._stream = stream
        self._streamStartIndex = 7
        self._classes = dict[str, GameDataClassDefinition]()
        self._counter = 0

        # Load the D2O
        stream.seek(0)
        self._stram = stream

        string_header = stream.readBytes(3)
        contentOffset = 0

        if string_header != b"D2O":
            self._stream.seek(0)
            string_header = stream.readUTF()
            if string_header != Signature.ANKAMA_SIGNED_FILE_HEADER:
                raise InvalidD2OFile("Malformated game data file.")
            stream.readShort()
            contentOffset = stream.readInt()
            self._stream.seek(contentOffset, 1)
            self._streamStartIndex = self._stream.position + 7
            string_header = stream.readBytes(3)
            if string_header != b"D2O":
                raise InvalidD2OFile("Malformated game data file.")

        indexesPointer = stream.readInt()
        self._stream.seek(contentOffset + indexesPointer)
        indexesLength = stream.readInt()

        self._indexes = OrderedDict()
        for _ in range(0, indexesLength, 8):
            key = stream.readInt()
            pointer = stream.readInt()
            self._indexes[key] = contentOffset + pointer
            self._counter += 1

        classesCount = stream.readInt()
        for _ in range(classesCount):
            classId = stream.readInt()
            self.readClassDefinition(classId, stream)

        if stream.remaining():
            self._gameDataProcessor = GameDataProcess(stream)

    def getObjects(self):
        if not self._counter:
            return None
        classCount = self._counter
        classes = self._classes
        stream = self._stram

        stream.seek(self._streamStartIndex)
        objects = list()
        for _ in range(classCount):
            classId = stream.readInt()
            instance = classes[classId].getInstance(stream)
            objects.append(instance)
        return objects

    def readClassDefinition(self, classId, stream: BinaryStream):
        className = stream.readUTF()
        packageName = stream.readUTF()
        classDef = GameDataClassDefinition(packageName, className, self)
        fieldsCount = stream.readInt()
        for _ in range(fieldsCount):
            field = stream.readUTF()
            classDef.addField(field, stream)
        self._classes[classId] = classDef

    def getClassDefinition(self, object_id: int) -> GameDataClassDefinition:
        return self._classes[object_id]

    def getObject(self, objectId: int) -> Any:
        if not self._indexes:
            return None
        pointer = self._indexes.get(objectId)
        if not pointer:
            return None
        self._stream.seek(pointer)
        classId: int = self._stream.readInt()
        return self._classes[classId].getInstance(self._stream)

    def close(self) -> None:
        for stream in self._streams:
            try:
                if isinstance(stream, BinaryStream):
                    stream.close()
            except Exception as e:
                continue
        self._streams = None
        self._indexes = None
        self._classes = None
