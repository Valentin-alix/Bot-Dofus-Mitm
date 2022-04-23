from com.ankamagames.jerakine.entities.interfaces.IEntity import IEntity


class IEntityLocalizer:
    def getEntity(self, param1: float) -> IEntity:
        pass

    def unregistered(self) -> None:
        pass
