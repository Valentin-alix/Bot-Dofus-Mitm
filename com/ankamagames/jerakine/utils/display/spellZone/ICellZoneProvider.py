from com.ankamagames.jerakine.utils.display.spellZone.IZoneShape import IZoneShape


class ICellZoneProvider:
    @property
    def minimalRange(self) -> int:
        pass

    @property
    def maximalRange(self) -> int:
        pass

    @property
    def castZoneInLine(self) -> bool:
        pass

    @property
    def spellZoneEffects(self) -> list[IZoneShape]:
        pass
