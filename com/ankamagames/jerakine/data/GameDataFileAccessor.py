from pathlib import Path
from typing import TYPE_CHECKING, Any
from com.ankamagames.dofus import Constants

if TYPE_CHECKING:
    from ankamagames.jerakine.data.GameDataProcess import GameDataProcess
    from ankamagames.jerakine.data.GameDataClassDefinition import (
        GameDataClassDefinition,
    )
from com.ankamagames.jerakine.data.ModuleReader import ModuleReader
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton
from com.ankamagames.jerakine.data.BinaryStream import BinaryStream


class GameDataFileAccessor(metaclass=Singleton):
    def __init__(self) -> None:
        self._modules = dict[str, ModuleReader]()

    def init(self, file: str) -> None:
        nativeFile = Path(file)
        moduleName: str = nativeFile.name.split(".d2o")[0]
        self._modules[moduleName] = ModuleReader(nativeFile.open("rb"))

    def initFromModuleName(self, moduleName: str) -> None:
        if moduleName not in self._modules:
            modle_file_path = Constants.DOFUS_COMMON_DIR / f"{moduleName}.d2o"
            self.init(modle_file_path)

    def initFromBinaryStream(self, modulename: str, moduleBinaries: BinaryStream):
        self._modules[modulename] = ModuleReader(moduleBinaries)

    def getDataProcessor(self, moduleName: str) -> "GameDataProcess":
        if moduleName not in self._modules:
            self.initFromModuleName(moduleName)
        return self._modules[moduleName]._gameDataProcessor

    def getClassDefinition(
        self, moduleName: str, classId: int
    ) -> "GameDataClassDefinition":
        return self._modules[moduleName]._classes[classId]

    def getCount(self, moduleName: str) -> int:
        if moduleName not in self._modules:
            self.initFromModuleName(moduleName)
        return self._modules[moduleName]._counter

    def getObject(self, moduleName: str, objectId) -> Any:
        return self._modules[moduleName].getObject(objectId)

    def getObjects(self, moduleName: str) -> list[object]:
        return self._modules[moduleName].getObjects()

    def close(self) -> None:
        for module in self._modules:
            self._modules[module].close()
        self._modules = dict[str, ModuleReader]()
