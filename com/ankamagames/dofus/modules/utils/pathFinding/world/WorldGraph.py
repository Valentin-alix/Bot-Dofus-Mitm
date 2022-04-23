from com.ankamagames.dofus.modules.utils.pathFinding.world.Edge import Edge
from com.ankamagames.dofus.modules.utils.pathFinding.world.Vertex import Vertex
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray


class WorldGraph:

    _vertices: dict[int, Vertex]

    _edges: dict[float, Edge]

    _outgoingEdges: dict

    _vertexUid: float = 0

    def __init__(self, data: ByteArray):
        self._vertices = dict()
        self._edges = dict()
        self._outgoingEdges = dict()
        edgeCount: int = data.readInt()
        for i in range(edgeCount):
            src = self.addVertex(data.readDouble(), data.readInt())
            dest = self.addVertex(data.readDouble(), data.readInt())
            edge = self.addEdge(src, dest)
            transitionCount = data.readInt()
            for j in range(transitionCount):
                edge.addTransition(
                    data.readByte(),
                    data.readByte(),
                    data.readInt(),
                    data.readUTFBytes(data.readInt()),
                    data.readDouble(),
                    data.readInt(),
                    data.readDouble(),
                )

    def getEdges(self) -> dict:
        return self._edges

    def addVertex(self, mapId: float, zone: int) -> Vertex:
        if self._vertices.get(mapId) is None:
            self._vertices[mapId] = dict()
        vertex: Vertex = self._vertices[mapId].get(zone)
        if vertex is None:
            vertex = Vertex(mapId, zone, self._vertexUid)
            self._vertexUid += 1
            self._vertices[mapId][zone] = vertex
        return vertex

    def getVertex(self, mapId: float, mapRpZone: int) -> Vertex:
        if self._vertices.get(mapId) is None:
            return None
        return self._vertices[mapId].get(mapRpZone)

    def getOutgoingEdgesFromVertex(self, src: Vertex) -> list[Edge]:
        return self._outgoingEdges[src.UID]

    def getEdge(self, src: Vertex, dest: Vertex) -> Edge:
        if self._edges.get(src.UID) == None:
            return None
        return self._edges[src.UID].get(dest.UID)

    def addEdge(self, src: Vertex, dest: Vertex) -> Edge:
        edge: Edge = self.getEdge(src, dest)
        if edge != None:
            return edge
        if not self.doesVertexExist(src) or not self.doesVertexExist(dest):
            return None
        edge = Edge(src, dest)
        if self._edges.get(src.UID) == None:
            self._edges[src.UID] = dict()
        self._edges[src.UID][dest.UID] = edge
        outgoing: list[Edge] = self._outgoingEdges.get(src.UID)
        if outgoing == None:
            outgoing = list[Edge]()
            self._outgoingEdges[src.UID] = outgoing
        outgoing.append(edge)
        return edge

    def doesVertexExist(self, v: Vertex) -> bool:
        return self._vertices[v.mapId][v.zoneId] != None
