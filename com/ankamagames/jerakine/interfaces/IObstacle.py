from abc import ABC


class IObstacle(ABC):
    def canSeeThrough(self) -> bool:
        pass

    def canWalkThrough(self) -> bool:
        pass

    def canWalkTo(self) -> bool:
        pass
