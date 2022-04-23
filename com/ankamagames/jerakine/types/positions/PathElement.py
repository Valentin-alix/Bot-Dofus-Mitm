from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint


class PathElement:
    def __init__(self, mp: MapPoint = None, orientation: int = 0):
        if mp is None:
            self.step = MapPoint()
        else:
            self.step = mp
        self._nOrientation = orientation

    @property
    def cellId(self):
        return self.step.cellId

    @property
    def orientation(self) -> int:
        return self._nOrientation

    @orientation.setter
    def orientation(self, value: int) -> None:
        self._nOrientation = value

    def __eq__(self, other) -> bool:
        return self.cellId == other.cellId and self.orientation == other.orientation

    def __str__(self) -> str:
        return "PE(cellId: {}, orientation: {})".format(self.cellId, self._nOrientation)
