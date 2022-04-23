import importlib
import sys
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ankamagames.jerakine.data.ModuleReader import ModuleReader
from com.ankamagames.jerakine.data.IposInit import IPostInit
from com.ankamagames.jerakine.data.BinaryStream import BinaryStream
from com.ankamagames.jerakine.data.GameDataField import GameDataField


class GameDataClassDefinition:
    def __init__(
        self, packageName: str, className: str, moduleReader: "ModuleReader"
    ) -> None:
        self._fields = list()
        moduleName = packageName + "." + className
        try:
            module = sys.modules[moduleName]
        except:
            module = importlib.import_module(moduleName)
        self._moduleName = moduleName
        self._name = className
        self._class = getattr(module, className)
        self._fields = list[GameDataField]()
        self.moduleReader = moduleReader

    @property
    def fields(self) -> list[GameDataField]:
        return self._fields

    def getInstance(self, stream: BinaryStream) -> Any:
        inst = self._class()
        for field in self._fields:
            attrib = field.name
            value = field.readData(stream)
            setattr(inst, attrib, value)
        if isinstance(inst, IPostInit):
            inst.postInit()
        return inst

    def addField(self, fileName: str, stream: BinaryStream) -> None:
        field = GameDataField(fileName, self.moduleReader)
        field.readType(stream)
        self._fields.append(field)
