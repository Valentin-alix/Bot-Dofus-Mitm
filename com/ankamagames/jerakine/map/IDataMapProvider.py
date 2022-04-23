class IDataMapProvider:
    @property
    def width(self) -> int:
        pass

    @property
    def height(self) -> int:
        pass

    def pointLos(self, param1: int, param2: int, param3: bool = True) -> bool:
        pass

    def pointMov(
        self,
        param1: int,
        param2: int,
        param3: bool = True,
        param4: int = -1,
        param5: int = -1,
        param6: bool = True,
    ) -> bool:
        pass

    def farmCell(self, param1: int, param2: int) -> bool:
        pass

    def pointSpecialEffects(self, param1: int, param2: int) -> int:
        pass

    def pointWeight(self, param1: int, param2: int, param3: bool = True) -> float:
        pass

    def hasEntity(self, param1: int, param2: int, param3: bool = False) -> bool:
        pass

    def updateCellMovLov(self, param1: int, param2: bool) -> None:
        pass

    def isChangeZone(self, param1: int, param2: int) -> bool:
        pass

    def getCellSpeed(self, param1: int) -> int:
        pass

    def fillEntityOnCelllist(self, param1: list[bool], param2: bool) -> list[bool]:
        pass
