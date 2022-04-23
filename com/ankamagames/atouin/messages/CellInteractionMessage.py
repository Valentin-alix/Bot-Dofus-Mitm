from com.ankamagames.atouin.messages.MapMessage import MapMessage
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint


class CellInteractionMessage(MapMessage):

    _cellId: int

    _cellDepth: int

    _cellCoords: MapPoint

    def __init__(self):
        super().__init__()

    @property
    def cellId(self) -> int:
        return self._cellId

    @cellId.setter
    def cellId(self, nValue: int) -> None:
        self._cellId = nValue

    @property
    def cellDepth(self) -> int:
        return self._cellDepth

    @cellDepth.setter
    def cellDepth(self, nValue: int) -> None:
        self._cellDepth = nValue

    @property
    def cell(self) -> MapPoint:
        return self._cellCoords

    @cell.setter
    def cell(self, pValue: MapPoint) -> None:
        self._cellCoords = pValue
