from com.ankamagames.jerakine.entities.interfaces.IEntity import IEntity
from com.ankamagames.jerakine.messages.Message import Message


class EntityMovementStoppedMessage(Message):

    _entity: IEntity

    id: float

    def __init__(self, entity: IEntity):
        super().__init__()
        self._entity = entity
        if self._entity:
            self.id = entity.id

    @property
    def entity(self) -> IEntity:
        return self._entity
