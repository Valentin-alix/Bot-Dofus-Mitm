from com.ankamagames.dofus.datacenter.world.MapPosition import MapPosition
from com.ankamagames.dofus.modules.utils.pathFinding.world.Vertex import Vertex


class Node:

    parent: "Node"

    vertex: Vertex

    map: MapPosition

    cost: int

    heuristic: int

    def __init__(
        self,
        vertex: Vertex,
        map: MapPosition,
        cost: int = 0,
        heuristic: int = 0,
        parent: "Node" = None,
    ):
        super().__init__()
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        self.map = map
        self.vertex = vertex
