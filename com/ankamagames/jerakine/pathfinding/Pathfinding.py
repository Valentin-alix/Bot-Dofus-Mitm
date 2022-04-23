import math

import mapTools.MapTools as MapTools
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.map.IDataMapProvider import IDataMapProvider
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint
from com.ankamagames.jerakine.types.positions.MovementPath import MovementPath
from com.ankamagames.jerakine.types.positions.PathElement import PathElement

logger = Logger(__name__)


class Pathfinding:

    HV_COST: int = 10

    DIAG_COST: int = 15

    HEURISTIC_COST: int = 10

    INFINITE_COST: int = 99999999

    _isInit: bool = False

    _parentOfCell = list[int]()

    _costOfCell = list[int]()

    _openListWeights = list[int]()

    _isCellClosed = list[bool]()

    _isEntityOnCell = list[bool]()

    _openList = list()

    def __init__(self):
        super().__init__()

    @classmethod
    def init(cls):
        cls._costOfCell = MapTools.mapCountCell * [None]
        cls._openListWeights = MapTools.mapCountCell * [0]
        cls._parentOfCell = MapTools.mapCountCell * [None]
        cls._isCellClosed = MapTools.mapCountCell * [None]
        cls._isEntityOnCell = MapTools.mapCountCell * [None]
        cls._openList = list()
        cls._isInit = True

    @classmethod
    def findPath(
        cls,
        mapData: IDataMapProvider,
        start: MapPoint,
        end: MapPoint,
        allowDiag: bool = True,
        bAllowTroughEntity: bool = True,
        aNoneObstacles: bool = True,
    ) -> MovementPath:
        endCellId: int = end.cellId
        startCellId: int = start.cellId
        endX: int = end.x
        endY: int = end.y
        endCellAuxId: int = startCellId
        distanceToEnd: int = MapTools.getDistance(startCellId, endCellId)
        if not cls._isInit:
            cls.init()
        for i in range(MapTools.mapCountCell):
            cls._parentOfCell[i] = MapTools.INVALID_CELL_ID
            cls._isCellClosed[i] = False
            cls._isEntityOnCell[i] = False
        cls._openList.clear()
        mapData.fillEntityOnCelllist(cls._isEntityOnCell, bAllowTroughEntity)
        cls._costOfCell[startCellId] = 0
        cls._openList.append(startCellId)
        while len(cls._openList) > 0 and cls._isCellClosed[endCellId] == False:
            minimum = cls.INFINITE_COST
            smallestCostIndex = 0
            for i in range(len(cls._openList)):
                cost = cls._openListWeights[cls._openList[i]]
                if cost <= minimum:
                    minimum = cost
                    smallestCostIndex = i
            parentId = cls._openList[smallestCostIndex]
            parentX = MapTools.getCellIdXCoord(parentId)
            parentY = MapTools.getCellIdYCoord(parentId)
            del cls._openList[smallestCostIndex]
            cls._isCellClosed[parentId] = True
            for y in range(parentY - 1, parentY + 2):
                for x in range(parentX - 1, parentX + 2):
                    cellId = MapTools.getCellIdByCoord(x, y)
                    if (
                        cellId != MapTools.INVALID_CELL_ID
                        and cls._isCellClosed[cellId] == False
                        and cellId != parentId
                        and mapData.pointMov(
                            x,
                            y,
                            bAllowTroughEntity,
                            parentId,
                            endCellId,
                            aNoneObstacles,
                        )
                        and (
                            y == parentY
                            or x == parentX
                            or allowDiag
                            and (
                                mapData.pointMov(
                                    parentX,
                                    y,
                                    bAllowTroughEntity,
                                    parentId,
                                    endCellId,
                                    aNoneObstacles,
                                )
                                or mapData.pointMov(
                                    x,
                                    parentY,
                                    bAllowTroughEntity,
                                    parentId,
                                    endCellId,
                                    aNoneObstacles,
                                )
                            )
                        )
                    ):
                        pointWeight = cls.getMapPointWeight(
                            mapData, cellId, endCellId, x, y, bAllowTroughEntity
                        )
                        movementCost = (
                            cls._costOfCell[parentId]
                            + (
                                cls.HV_COST
                                if y == parentY or x == parentX
                                else cls.DIAG_COST
                            )
                            * pointWeight
                        )
                        if bAllowTroughEntity:
                            cellOnEndColumn = x + y == endX + endY
                            cellOnStartColumn = x + y == start.x + start.y
                            cellOnEndLine = x - y == endX - endY
                            cellOnStartLine = x - y == start.x - start.y
                            if (
                                not cellOnEndColumn
                                and not cellOnEndLine
                                or not cellOnStartColumn
                                and not cellOnStartLine
                            ):
                                movementCost += MapTools.getDistance(cellId, endCellId)
                                movementCost += MapTools.getDistance(
                                    cellId, startCellId
                                )
                            if x == endX or y == endY:
                                movementCost -= 3
                            if (
                                cellOnEndColumn
                                or cellOnEndLine
                                or x + y == parentX + parentY
                                or x - y == parentX - parentY
                            ):
                                movementCost -= 2
                            if i == start.x or y == start.y:
                                movementCost -= 3
                            if cellOnStartColumn or cellOnStartLine:
                                movementCost -= 2
                            distanceTmpToEnd = MapTools.getDistance(cellId, endCellId)
                            if distanceTmpToEnd < distanceToEnd:
                                endCellAuxId = cellId
                                distanceToEnd = distanceTmpToEnd
                        if (
                            cls._parentOfCell[cellId] == MapTools.INVALID_CELL_ID
                            or movementCost < cls._costOfCell[cellId]
                        ):
                            cls._parentOfCell[cellId] = parentId
                            cls._costOfCell[cellId] = movementCost
                            heuristic = cls.HEURISTIC_COST * math.sqrt(
                                (endY - y) * (endY - y) + (endX - x) * (endX - x)
                            )
                            cls._openListWeights[cellId] = heuristic + movementCost
                            if cellId not in cls._openList:
                                cls._openList.append(cellId)
        if cls._isCellClosed[endCellId] == True:
            logger.info("Path to dest found")
        else:
            logger.error("Path to dest not found")
        movPath: MovementPath = MovementPath()
        movPath.start = start
        if cls._parentOfCell[endCellId] == MapTools.INVALID_CELL_ID:
            endCellId = endCellAuxId
            movPath.end = MapPoint.fromCellId(endCellId)
        else:
            movPath.end = end
        cursor = endCellId
        MAX_IT = 200
        currIt = 0
        while cursor != startCellId:
            currIt = currIt + 1
            if currIt > MAX_IT:
                raise Exception("Max iterations reached")
            if allowDiag:
                parent = cls._parentOfCell[cursor]
                grandParent = (
                    int(MapTools.INVALID_CELL_ID)
                    if parent == MapTools.INVALID_CELL_ID
                    else int(cls._parentOfCell[parent])
                )
                grandGrandParent = (
                    int(MapTools.INVALID_CELL_ID)
                    if grandParent == MapTools.INVALID_CELL_ID
                    else int(cls._parentOfCell[grandParent])
                )
                kX = MapTools.getCellIdXCoord(cursor)
                kY = MapTools.getCellIdYCoord(cursor)
                if (
                    grandParent != MapTools.INVALID_CELL_ID
                    and MapTools.getDistance(cursor, grandParent) == 1
                ):
                    if mapData.pointMov(
                        kX, kY, bAllowTroughEntity, grandParent, endCellId
                    ):
                        cls._parentOfCell[cursor] = grandParent
                elif (
                    grandGrandParent != MapTools.INVALID_CELL_ID
                    and MapTools.getDistance(cursor, grandGrandParent) == 2
                ):
                    nextX = MapTools.getCellIdXCoord(grandGrandParent)
                    nextY = MapTools.getCellIdYCoord(grandGrandParent)
                    interX = kX + round((nextX - kX) / 2)
                    interY = kY + round((nextY - kY) / 2)
                    if (
                        mapData.pointMov(
                            interX, interY, bAllowTroughEntity, cursor, endCellId
                        )
                        and mapData.pointWeight(interX, interY) < 2
                    ):
                        cls._parentOfCell[cursor] = MapTools.getCellIdByCoord(
                            interX, interY
                        )
                elif (
                    grandParent != MapTools.INVALID_CELL_ID
                    and MapTools.getDistance(cursor, grandParent) == 2
                ):
                    nextX = MapTools.getCellIdXCoord(grandParent)
                    nextY = MapTools.getCellIdYCoord(grandParent)
                    interX = MapTools.getCellIdXCoord(parent)
                    interY = MapTools.getCellIdYCoord(parent)
                    if (
                        kX + kY == nextX + nextY
                        and kX - kY != interX - interY
                        and not mapData.isChangeZone(
                            MapTools.getCellIdByCoord(kX, kY),
                            MapTools.getCellIdByCoord(interX, interY),
                        )
                        and not mapData.isChangeZone(
                            MapTools.getCellIdByCoord(interX, interY),
                            MapTools.getCellIdByCoord(nextX, nextY),
                        )
                    ):
                        cls._parentOfCell[cursor] = grandParent
                    elif (
                        kX - kY == nextX - nextY
                        and kX - kY != interX - interY
                        and not mapData.isChangeZone(
                            MapTools.getCellIdByCoord(kX, kY),
                            MapTools.getCellIdByCoord(interX, interY),
                        )
                        and not mapData.isChangeZone(
                            MapTools.getCellIdByCoord(interX, interY),
                            MapTools.getCellIdByCoord(nextX, nextY),
                        )
                    ):
                        cls._parentOfCell[cursor] = grandParent
                    elif (
                        kX == nextX
                        and kX != interX
                        and mapData.pointWeight(kX, interY) < 2
                        and mapData.pointMov(
                            kX, interY, bAllowTroughEntity, cursor, endCellId
                        )
                    ):
                        cls._parentOfCell[cursor] = MapTools.getCellIdByCoord(
                            kX, interY
                        )
                    elif (
                        kY == nextY
                        and kY != interY
                        and mapData.pointWeight(interX, kY) < 2
                        and mapData.pointMov(
                            interX, kY, bAllowTroughEntity, cursor, endCellId
                        )
                    ):
                        cls._parentOfCell[cursor] = MapTools.getCellIdByCoord(
                            interX, kY
                        )
            movPath.addPoint(
                PathElement(
                    MapPoint.fromCellId(cls._parentOfCell[cursor]),
                    MapTools.getLookDirection8Exact(cls._parentOfCell[cursor], cursor),
                )
            )
            cursor = cls._parentOfCell[cursor]
        movPath.path.reverse()
        # logger.debug("Path found : " + str(movPath))
        return movPath

    @classmethod
    def getMapPointWeight(
        cls, mapData: IDataMapProvider, cellId, endCellId, x, y, bAllowTroughEntity
    ):
        pointWeight = 0
        if cellId == endCellId:
            pointWeight = 1
        else:
            speed = mapData.getCellSpeed(cellId)
            if bAllowTroughEntity:
                if cls._isEntityOnCell[cellId]:
                    pointWeight = 20
                elif speed >= 0:
                    pointWeight = 6 - speed
                else:
                    pointWeight = 12 + abs(speed)
            else:
                pointWeight = 1
                if cls._isEntityOnCell[cellId]:
                    pointWeight += 0.3
                if (
                    MapTools.isValidCoord(x + 1, y)
                    and cls._isEntityOnCell[MapTools.getCellIdByCoord(x + 1, y)]
                ):
                    pointWeight += 0.3
                if (
                    MapTools.isValidCoord(x, y + 1)
                    and cls._isEntityOnCell[MapTools.getCellIdByCoord(x, y + 1)]
                ):
                    pointWeight += 0.3
                if (
                    MapTools.isValidCoord(x - 1, y)
                    and cls._isEntityOnCell[MapTools.getCellIdByCoord(x - 1, y)]
                ):
                    pointWeight += 0.3
                if (
                    MapTools.isValidCoord(x, y - 1)
                    and cls._isEntityOnCell[MapTools.getCellIdByCoord(x, y - 1)]
                ):
                    pointWeight += 0.3
                if mapData.pointSpecialEffects(x, y) & 2 == 2:
                    pointWeight += 0.2
        return pointWeight
