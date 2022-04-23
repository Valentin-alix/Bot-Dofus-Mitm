from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint


class IEntity:
    @property
    def id(self) -> int:
        pass

    @id.setter
    def id(self, param1: int) -> None:
        pass

    @property
    def position(self) -> MapPoint:
        pass

    @position.setter
    def position(self, param1: MapPoint) -> None:
        pass
