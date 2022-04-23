from com.ankamagames.jerakine.entities.interfaces.IEntity import IEntity
from com.ankamagames.jerakine.messages.Message import Message


class EntityMovementCompleteMessage(Message):
    def __init__(self, entity: IEntity = None):
        super().__init__()
        self._entity = entity
        if self._entity:
            self.id = entity.id

    @property
    def entity(self) -> IEntity:
        return self._entity
