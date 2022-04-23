from com.ankamagames.atouin.AtouinConstants import AtouinConstants
from com.ankamagames.atouin.data.map.MapZones import MapZones
from com.ankamagames.atouin.data.map.Fixture import Fixture
from com.ankamagames.atouin.data.map.Cell import Cell
from com.ankamagames.atouin.data.map.Layer import Layer
from com.ankamagames.atouin.utils.CellIdConverter import CellIdConverter
from com.ankamagames.jerakine.data.BinaryStream import BinaryStream
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.types.enums.DirectionsEnum import DirectionsEnum
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint

logger = Logger(__name__)


class Map:
    def __init__(self, raw: BinaryStream, id, version: int):
        self.id = id
        self.version = version
        self.topArrowCell = set[int]()
        self.bottomArrowCell = set[int]()
        self.leftArrowCell = set[int]()
        self.rightArrowCell = set[int]()
        self.cells = dict[int, Cell]()
        self.oldMvtSystem = False
        self.isUsingNewMovementSystem = False
        self._parser = False
        self.fromRaw(raw)
        self.zones = MapZones(self)

    def fromRaw(self, raw: BinaryStream):
        self.relativeId = raw.readUnsignedInt()
        self.mapType = raw.readByte()
        self.subareaId = raw.readInt()
        self.topNeighbourId = raw.readInt()
        self.bottomNeighbourId = raw.readInt()
        self.leftNeighbourId = raw.readInt()
        self.rightNeighbourId = raw.readInt()
        self.shadowBonusOnEntities = raw.readUnsignedInt()

        if self.version >= 9:
            read_color = raw.readInt()
            self.backgroundAlpha = (read_color & 4278190080) >> 32
            self.backgroundRed = (read_color & 16711680) >> 16
            self.backgroundGreen = (read_color & 65280) >> 8
            self.backgroundBlue = read_color & 255
            read_color = raw.readUnsignedInt()
            grid_alpha = (read_color & 4278190080) >> 32
            grid_red = (read_color & 16711680) >> 16
            grid_green = (read_color & 65280) >> 8
            grid_blue = read_color & 255
            self.gridColor = (
                (grid_alpha & 255) << 32
                | (grid_red & 255) << 16
                | (grid_green & 255) << 8
                | grid_blue & 255
            )

        elif self.version >= 3:
            self.backgroundRed = raw.readByte()
            self.backgroundGreen = raw.readByte()
            self.backgroundBlue = raw.readByte()

        self.backgroundColor = (
            (self.backgroundAlpha & 255) << 32
            | (self.backgroundRed & 255) << 16
            | (self.backgroundGreen & 255) << 8
            | self.backgroundBlue & 255
        )

        if self.version >= 4:
            self.zoomScale = raw.readUnsignedShort() // 100
            self.zoomOffsetX = raw.readShort()
            self.zoomOffsetY = raw.readShort()
            if self.zoomScale < 1:
                self.zoomScale = 1
                self.zoomOffsetX = self.zoomOffsetY = 0

        if self.version > 10:
            self.tacticalModeTemplateId = raw.readInt()

        self.backgroundsCount = raw.readByte()
        self.backgroundFixtures = [Fixture(raw) for _ in range(self.backgroundsCount)]

        self.foregroundsCount = raw.readByte()
        self.foregroundsFixtures = [Fixture(raw) for _ in range(self.foregroundsCount)]

        raw.readInt()
        self.groundCRC = raw.readInt()
        self.layersCount = raw.readByte()
        self.layers = [Layer(raw, self.version) for _ in range(self.layersCount)]

        for cellid in range(AtouinConstants.MAP_CELLS_COUNT):
            cell = Cell(raw, self, cellid)
            self.cells[cellid] = cell

            if not self.oldMvtSystem:
                self.oldMvtSystem = cell.moveZone
            if cell.moveZone != self.oldMvtSystem:
                self.isUsingNewMovementSystem = True

            if cell.top_arrow:
                self.topArrowCell.add(cellid)

            elif cell.bottom_arrow:
                self.bottomArrowCell.add(cellid)

            elif cell.left_arrow:
                self.leftArrowCell.add(cellid)

            elif cell.right_arrow:
                self.rightArrowCell.add(cellid)

        self._parser = True

    def getOutgoingCells(self, direction: DirectionsEnum):
        return set(
            [i for i in self.OUTCELLS[direction] if self.cells[i].allowsMapChange()]
        )

    def cellOutTowards(self, currCellId, direction: DirectionsEnum):
        currZone = self.zones.getZone(currCellId)
        condidateOutCells = self.getBorderCells(direction)
        mindDist = float("inf")
        outCellId = None
        for cellid in condidateOutCells:
            if self.zones.getZone(cellid) == currZone:
                mp1 = MapPoint.fromCellId(currCellId)
                mp2 = MapPoint.fromCellId(cellid)
                dist = mp1.distanceToCell(mp2)
                if dist < mindDist:
                    mindDist = dist
                    outCellId = cellid
        return outCellId

    def getNeighbourCellFromDirection(
        cls, srcId: int, direction: DirectionsEnum
    ) -> "Cell":
        if (srcId // AtouinConstants.MAP_WIDTH) % 2 == 0:
            offsetId = 0

        else:
            offsetId = 1

        if direction == DirectionsEnum.RIGHT:
            destId = srcId + 1
            if destId % AtouinConstants.MAP_WIDTH != 0:
                return cls.cells[destId]
            return None

        elif direction == DirectionsEnum.DOWN_RIGHT:
            destId = srcId + AtouinConstants.MAP_WIDTH + offsetId
            if (
                destId < AtouinConstants.MAP_CELLS_COUNT
                and (srcId + 1) % (AtouinConstants.MAP_WIDTH * 2) != 0
            ):
                return cls.cells[destId]
            return None

        elif direction == DirectionsEnum.DOWN:
            destId = srcId + AtouinConstants.MAP_WIDTH * 2
            if destId < AtouinConstants.MAP_CELLS_COUNT:
                return cls.cells[destId]
            return None

        elif direction == DirectionsEnum.DOWN_LEFT:
            destId = srcId + AtouinConstants.MAP_WIDTH - 1 + offsetId
            if (
                destId < AtouinConstants.MAP_CELLS_COUNT
                and srcId % (AtouinConstants.MAP_WIDTH * 2) != 0
            ):
                return cls.cells[destId]
            return None

        elif direction == DirectionsEnum.LEFT:
            destId = srcId - 1
            if srcId % AtouinConstants.MAP_WIDTH != 0:
                return cls.cells[destId]
            return None

        elif direction == DirectionsEnum.UP_LEFT:
            destId = srcId - AtouinConstants.MAP_WIDTH - 1 + offsetId
            if destId >= 0 and srcId % (AtouinConstants.MAP_WIDTH * 2) != 0:
                return cls.cells[destId]
            return None

        elif direction == DirectionsEnum.UP:
            destId = srcId - AtouinConstants.MAP_WIDTH * 2
            if destId >= 0:
                return cls.cells[destId]
            return None

        elif direction == DirectionsEnum.UP_RIGHT:
            destId = srcId - AtouinConstants.MAP_WIDTH + offsetId
            if destId > 0 and (srcId + 1) % (AtouinConstants.MAP_WIDTH * 2) != 0:
                return cls.cells[destId]
            return None

        raise Exception("Invalid direction.")

    def getCellNeighbours(self, cellId: int) -> set["Cell"]:
        neighbours = set[Cell]()
        for i in DirectionsEnum:
            cell = self.getNeighbourCellFromDirection(cellId, i)
            if cell and cell.isAccessibleDuringRP():
                neighbours.add(cell)
        return neighbours

    def getNeighborIdFromDirection(self, direction: DirectionsEnum) -> int:
        if direction == DirectionsEnum.LEFT:
            return self.leftNeighbourId
        elif direction == DirectionsEnum.RIGHT:
            return self.rightNeighbourId
        elif direction == DirectionsEnum.UP:
            return self.topNeighbourId
        elif direction == DirectionsEnum.DOWN:
            return self.bottomNeighbourId
        else:
            raise Exception("invalid direction : " + str(direction))

    def printGrid(self):
        format_row = "{:>2}" * (AtouinConstants.MAP_WIDTH + 2)
        print(format_row.format(*[" "] * (AtouinConstants.MAP_WIDTH + 2)))
        for j in range(2 * AtouinConstants.MAP_HEIGHT):
            row = []
            for i in range(AtouinConstants.MAP_WIDTH):
                row.append(
                    " "
                    if self.cells[
                        i + j * AtouinConstants.MAP_WIDTH
                    ].isAccessibleDuringRP()
                    else "X"
                )
            print(format_row.format(" ", *row, " "))
        print(format_row.format(*[" "] * (AtouinConstants.MAP_WIDTH + 2)))

    def getBorderCells(self, direction: DirectionsEnum):
        currentlyCheckedCellX = None
        currentlyCheckedCellY = None

        if direction == DirectionsEnum.RIGHT:
            currentlyCheckedCellX = AtouinConstants.MAP_WIDTH - 1
            currentlyCheckedCellY = AtouinConstants.MAP_WIDTH - 1

        elif direction == DirectionsEnum.LEFT:
            currentlyCheckedCellX = 0
            currentlyCheckedCellY = 0

        elif direction == DirectionsEnum.DOWN:
            currentlyCheckedCellX = AtouinConstants.MAP_HEIGHT - 1
            currentlyCheckedCellY = -(AtouinConstants.MAP_HEIGHT - 1)

        elif direction == DirectionsEnum.UP:
            currentlyCheckedCellX = 0
            currentlyCheckedCellY = 0

        res = []

        if direction == DirectionsEnum.RIGHT or direction == DirectionsEnum.LEFT:
            maxI = AtouinConstants.MAP_HEIGHT * 2
            for i in range(maxI):
                currentCellId = MapPoint.fromCoords(
                    currentlyCheckedCellX, currentlyCheckedCellY
                ).cellId
                cellData = self.cells[currentCellId]
                mapChangeData = cellData.mapChangeData
                if mapChangeData and (
                    direction == DirectionsEnum.RIGHT
                    and (
                        mapChangeData & 1
                        or (currentCellId + 1) % (AtouinConstants.MAP_WIDTH * 2) == 0
                        and mapChangeData & 2
                        or (currentCellId + 1) % (AtouinConstants.MAP_WIDTH * 2) == 0
                        and mapChangeData & 128
                    )
                    or direction == DirectionsEnum.LEFT
                    and (
                        currentlyCheckedCellX == -currentlyCheckedCellY
                        and mapChangeData & 8
                        or mapChangeData & 16
                        or currentlyCheckedCellX == -currentlyCheckedCellY
                        and mapChangeData & 32
                    )
                ):
                    res.append(currentCellId)
                if not (i % 2):
                    currentlyCheckedCellX += 1
                else:
                    currentlyCheckedCellY -= 1

        elif direction == DirectionsEnum.DOWN or direction == DirectionsEnum.UP:
            for i in range(AtouinConstants.MAP_WIDTH * 2):
                currentCellId = MapPoint.fromCoords(
                    currentlyCheckedCellX, currentlyCheckedCellY
                ).cellId
                cellData = self.cells[currentCellId]
                mapChangeData = cellData.mapChangeData
                if mapChangeData and (
                    direction == DirectionsEnum.UP
                    and (
                        currentCellId < AtouinConstants.MAP_WIDTH
                        and mapChangeData & 32
                        or mapChangeData & 64
                        or currentCellId < AtouinConstants.MAP_WIDTH
                        and mapChangeData & 128
                    )
                    or direction == DirectionsEnum.DOWN
                    and (
                        currentCellId
                        >= AtouinConstants.MAP_CELLS_COUNT - AtouinConstants.MAP_WIDTH
                        and mapChangeData & 2
                        or mapChangeData & 4
                        or currentCellId
                        >= AtouinConstants.MAP_CELLS_COUNT - AtouinConstants.MAP_WIDTH
                        and mapChangeData & 8
                    )
                ):
                    res.append(currentCellId)
                if not (i % 2):
                    currentlyCheckedCellX += 1
                else:
                    currentlyCheckedCellY += 1

        return res
