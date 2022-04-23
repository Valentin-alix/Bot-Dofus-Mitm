from time import perf_counter
from types import FunctionType
from whistle import Event
from com.ankamagames.dofus.datacenter.world.MapPosition import MapPosition
from com.ankamagames.dofus.datacenter.world.SubArea import SubArea
from com.ankamagames.dofus.misc.utils.GameDataQuery import GameDataQuery
from com.ankamagames.dofus.modules.utils.pathFinding.world.Edge import Edge
from com.ankamagames.dofus.modules.utils.pathFinding.world.Node import Node
from com.ankamagames.dofus.modules.utils.pathFinding.world.Vertex import Vertex
from com.ankamagames.dofus.modules.utils.pathFinding.world.WorldGraph import WorldGraph
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.utils.display.EnterFrameConst import EnterFrameConst
from com.ankamagames.jerakine.utils.display.EnterFrameDispatcher import (
    EnterFrameDispatcher,
)

logger = Logger(__name__)


class AStar:
    DEBUG = True
    dest: MapPosition = None

    closedDic = dict()

    openList = list[Node]()

    openDic = dict()

    iterations: int = 0

    worldGraph: WorldGraph = None

    dst: Vertex = None

    callback: FunctionType = None

    _forbiddenSubareaIds = list[int]()

    HEURISTIC_SCALE: int = 1

    INDOOR_WEIGHT: int = 0

    MAX_ITERATION: int = 10000

    def __init__(self):
        super().__init__()

    @classmethod
    def search(
        cls, worldGraph: WorldGraph, src: Vertex, dst: Vertex, callback: FunctionType
    ) -> None:
        if cls.DEBUG:
            logger.debug(f"Searching path from {src} to {dst} ...")
        if cls.callback != None:
            raise Exception("Pathfinding already in progress")
        if src == dst:
            callback(None)
            return
        cls.initForbiddenSubareaList()
        cls.worldGraph = worldGraph
        cls.dst = dst
        cls.callback = callback
        cls.dest = MapPosition.getMapPositionById(dst.mapId)
        cls.closedDic = dict()
        cls.openList = list[Node]()
        cls.openDic = dict()
        cls.iterations = 0
        cls.openList.append(Node(src, MapPosition.getMapPositionById(src.mapId)))
        EnterFrameDispatcher().addEventListener(
            cls.compute, EnterFrameConst.COMPUTE_ASTAR
        )

    @classmethod
    def initForbiddenSubareaList(cls) -> None:
        cls._forbiddenSubareaIds = GameDataQuery.queryEquals(
            SubArea, "mountAutoTripAllowed", False
        )

    @classmethod
    def stopSearch(cls) -> None:
        if cls.callback != None:
            cls.callbackWithResult(None)

    @classmethod
    def compute(cls, e: Event = None) -> None:
        if cls.DEBUG:
            logger.debug(f"Iteration {cls.iterations}")
        while cls.openList:
            if cls.iterations > cls.MAX_ITERATION:
                cls.callbackWithResult(None)
                logger.error("Too many iterations, aborting A*")
                return
            cls.iterations += 1
            current = cls.openList.pop(0)
            cls.openDic[current.vertex] = None
            if current.vertex == cls.dst:
                logger.debug("Goal reached with " + str(cls.iterations) + " iterations")
                cls.callbackWithResult(cls.buildResultPath(cls.worldGraph, current))
                return
            edges = cls.worldGraph.getOutgoingEdgesFromVertex(current.vertex)
            oldLength = len(cls.openList)
            cost = current.cost + 1
            for edge in edges:
                if cls.hasValidTransition(edge):
                    if cls.hasValidDestinationSubarea(edge):
                        existing = cls.closedDic.get(edge.dst)
                        if not (existing != None and cost >= existing.cost):
                            existing = cls.openDic.get(edge.dst)
                            if not (existing != None and cost >= existing.cost):
                                map = MapPosition.getMapPositionById(edge.dst.mapId)
                                if map == None:
                                    logger.info(
                                        "La map "
                                        + edge.dst.mapId
                                        + " ne semble pas exister"
                                    )
                                else:
                                    manhattanDistance = abs(
                                        map.posX - cls.dest.posX
                                    ) + abs(map.posY - cls.dest.posY)
                                    node = Node(
                                        edge.dst,
                                        map,
                                        cost,
                                        cost
                                        + cls.HEURISTIC_SCALE * manhattanDistance
                                        + (
                                            cls.INDOOR_WEIGHT
                                            if current.map.outdoor and not map.outdoor
                                            else 0
                                        ),
                                        current,
                                    )
                                    cls.openList.append(node)
                                    cls.openDic[node.vertex] = node
            cls.closedDic[current.vertex] = current
            if oldLength < len(cls.openList):
                cls.openList.sort(key=lambda x: x.heuristic)
        cls.callbackWithResult(None)

    @staticmethod
    def hasValidTransition(edge: Edge) -> bool:
        from com.ankamagames.dofus.datacenter.items.criterion.GroupItemCriterion import (
            GroupItemCriterion,
        )

        criterionWhiteList: list = [
            "Ad",
            "DM",
            "MI",
            "Mk",
            "Oc",
            "Pc",
            "QF",
            "Qo",
            "Qs",
            "Sv",
        ]
        valid: bool = False
        for transition in edge.transitions:
            if len(transition.criterion) != 0:
                if (
                    "&" not in transition.criterion
                    and "|" not in transition.criterion
                    and transition.criterion[0:2] not in criterionWhiteList
                ):
                    return False
                criterion = GroupItemCriterion(transition.criterion)
                return criterion.isRespected
            valid = True
        return valid

    @classmethod
    def hasValidDestinationSubarea(cls, edge: Edge) -> bool:
        fromMapId: float = edge.src.mapId
        fromSubareaId: int = MapPosition.getMapPositionById(fromMapId).subAreaId
        toMapId: float = edge.dst.mapId
        toSubareaId: int = MapPosition.getMapPositionById(toMapId).subAreaId
        if fromSubareaId == toSubareaId:
            return True
        return toSubareaId not in cls._forbiddenSubareaIds

    @classmethod
    def callbackWithResult(cls, result: list[Edge]) -> None:
        cb: FunctionType = cls.callback
        cls.callback = None
        EnterFrameDispatcher().removeEventListener(cls.compute)
        cb(result)

    @classmethod
    def orderNodes(cls, a: Node, b: Node) -> int:
        return (
            0
            if a.heuristic == b.heuristic
            else (1 if a.heuristic > b.heuristic else -1)
        )

    @classmethod
    def buildResultPath(cls, worldGraph: WorldGraph, node: Node) -> list[Edge]:
        result = list[Edge]()
        while node.parent != None:
            result.append(worldGraph.getEdge(node.parent.vertex, node.vertex))
            node = node.parent
        result.reverse()
        return result
