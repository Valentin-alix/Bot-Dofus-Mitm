from com.ankamagames.dofus.modules.utils.pathFinding.world.Transition import Transition
from com.ankamagames.dofus.modules.utils.pathFinding.world.Vertex import Vertex


class Edge:
    _src: Vertex

    _dst: Vertex

    _transitions: list[Transition]

    def __init__(self, src: Vertex, dst: Vertex):
        super().__init__()
        self._src = src
        self._dst = dst
        self._transitions = list[Transition]()

    @property
    def src(self) -> Vertex:
        return self._src

    @property
    def dst(self) -> Vertex:
        return self._dst

    @property
    def transitions(self) -> list[Transition]:
        return self._transitions

    def addTransition(
        self,
        dir: int,
        type: int,
        skill: int,
        criterion: str,
        transitionMapId: float,
        cell: int,
        id: int,
    ) -> None:
        self.transitions.append(
            Transition(type, dir, skill, criterion, transitionMapId, cell, id)
        )

    def __str__(self):
        return "Edge(src={}, dst={}, transitions={})".format(
            self.src, self.dst, self.transitions
        )
