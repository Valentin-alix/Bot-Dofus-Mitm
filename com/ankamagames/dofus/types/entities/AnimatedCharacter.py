from com.ankamagames.jerakine.entities.interfaces.IEntity import IEntity
from com.ankamagames.jerakine.interfaces.IObstacle import IObstacle
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint


class AnimatedCharacter(IEntity, IObstacle):
    def __init__(self, id: int):
        self._id = id
        self._position = None
        self._name = ""
        self._canSeeThrough: bool = False
        self._canWalkThrough: bool = False
        self._canWalkTo: bool = False
        self._isMoving = False
        self._stop = False
        self.speedAdjust: float = 0.0
        self.cantWalk8Directions: bool = False
        super().__init__()

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def position(self) -> MapPoint:
        return self._position

    @position.setter
    def position(self, value: MapPoint):
        self._position = value

    @property
    def canSeeThrough(self) -> bool:
        return self._canSeeThrough

    @canSeeThrough.setter
    def canSeeThrough(self, value: bool) -> None:
        self._canSeeThrough = value

    @property
    def canWalkThrough(self) -> bool:
        return self._canWalkThrough

    @canWalkThrough.setter
    def canWalkThrough(self, value: bool) -> None:
        self._canWalkThrough = value

    @property
    def canWalkTo(self) -> bool:
        return self._canWalkThrough

    @canWalkTo.setter
    def canWalkTo(self, value: bool) -> None:
        self._canWalkTo = value

    @property
    def isMoving(self) -> bool:
        return self._isMoving

    @isMoving.setter
    def isMoving(self, value: bool) -> None:
        self._isMoving = value

    @property
    def stop(self) -> bool:
        return self._stop

    @stop.setter
    def stop(self, value: bool) -> None:
        self._stop = value
