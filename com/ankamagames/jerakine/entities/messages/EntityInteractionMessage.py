from com.ankamagames.jerakine.entities.interfaces.IInteractive import IInteractive
from com.ankamagames.jerakine.messages.Message import Message


class EntityInteractionMessage(Message):

    _entity: IInteractive

    def __init__(self, entity: IInteractive):
        super().__init__()
        self._entity = entity

    @property
    def entity(self) -> IInteractive:
        return self._entity
