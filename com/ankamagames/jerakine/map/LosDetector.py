import math
from com.ankamagames.atouin.data.map.map import Map
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint
from mapTools import MapTools


def getRange(refPosition: MapPoint, po: int) -> list[int]:
    res = list[MapPoint]()
    for i in range(po):
        for j in range(po):
            if abs(i - refPosition.x) + abs(j - refPosition.y) <= po:
                res.append(MapPoint.fromCoords(i, j))
    return res


def getCell(
    mapData: Map, spellrange: list[MapPoint], refPosition: MapPoint
) -> list[int]:
    orderedCell: list = list()
    for mp in spellrange:
        orderedCell.append({"p": mp, "dist": refPosition.distanceToCell(mp)})
    sorted(orderedCell, key=lambda x: x["dist"], reverse=True)
    tested = dict[str, bool]()
    result: list[int] = list[int]()
    for i in range(len(orderedCell)):
        p: MapPoint = orderedCell[i]["p"]

        if (
            tested.get(f"{p.x}_{p.y}") is None
            or refPosition.x + refPosition.y == p.x + p.y
            or refPosition.x - refPosition.y == p.x - p.y
        ):
            line = MapTools.getCellsCoordBetween(refPosition.cellId, p.cellId)
            if len(line) == 0:
                result.append(p.cellId)

            else:
                los = True
                for j in range(len(line)):
                    currentPoint = (
                        str(math.floor(line[j].x)) + "_" + str(math.floor(line[j].y))
                    )
                    if MapPoint.isInMap(line[j].x, line[j].y):
                        if j > 0 and mapData.hasEntity(
                            math.floor(line[j - 1].x), math.floor(line[j - 1].y)
                        ):
                            los = False

                        elif (
                            line[j].x + line[j].y == refPosition.x + refPosition.y
                            or line[j].x - line[j].y == refPosition.x - refPosition.y
                        ):
                            los = los and mapData.pointLos(
                                math.floor(line[j].x), math.floor(line[j].y)
                            )

                        elif tested.get(currentPoint) is None:
                            los = los and mapData.pointLos(
                                math.floor(line[j].x), math.floor(line[j].y)
                            )

                        else:
                            los = los and tested[currentPoint]
                tested[currentPoint] = los

    for mp in spellrange:
        if tested[mp.x + "_" + mp.y]:
            result.append(mp.cellId)

    return result
