from com.ankamagames.jerakine.utils.display.spellZone.IZoneShape import IZoneShape


class ZoneEffect(IZoneShape):

    _zoneSize: int

    _zoneShape: int

    def __init__(self, zsize: int, zshape: int):
        super().__init__()
        self._zoneSize = zsize
        self._zoneShape = zshape

    @property
    def zoneSize(self) -> int:
        return self._zoneSize

    @zoneSize.setter
    def zoneSize(self, pZoneSize: int) -> None:
        self._zoneSize = pZoneSize

    @property
    def zoneShape(self) -> int:
        return self._zoneShape

    @zoneShape.setter
    def zoneShape(self, pZoneShape: int) -> None:
        self._zoneShape = pZoneShape
