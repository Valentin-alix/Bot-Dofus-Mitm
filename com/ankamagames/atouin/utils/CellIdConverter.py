from com.ankamagames.atouin.AtouinConstants import AtouinConstants
from com.ankamagames.jerakine.types.positions.MapPoint import Point


class CellIdConverter:

    CELLPOS: list = list()

    _bInit: bool = False

    def __init__(self):
        super().__init__()

    @classmethod
    def init(cls) -> None:
        b: int = 0
        cls._bInit = True
        startX: int = 0
        startY: int = 0
        cell: int = 0
        for a in range(AtouinConstants.MAP_HEIGHT):
            for b in range(AtouinConstants.MAP_WIDTH):
                cls.CELLPOS[cell] = Point(startX + b, startY + b)
                cell += 1
            startX += 1
            for b in range(AtouinConstants.MAP_WIDTH):
                cls.CELLPOS[cell] = Point(startX + b, startY + b)
                cell += 1
            startY -= 1

    @classmethod
    def coordToCellId(cls, x: int, y: int) -> int:
        if not cls._bInit:
            cls.init()
        return (x - y) * AtouinConstants.MAP_WIDTH + y + (x - y) / 2

    @classmethod
    def cellIdToCoord(cls, cellId: int) -> Point:
        if not cls._bInit:
            cls.init()
        if not cls.CELLPOS[cellId]:
            return None
        return cls.CELLPOS[cellId]
