from com.ankamagames.jerakine.entities.interfaces.IInteractive import IInteractive
from com.ankamagames.jerakine.entities.messages.EntityInteractionMessage import (
    EntityInteractionMessage,
)


class EntityClickMessage(EntityInteractionMessage):

    fromStack: bool

    def __init__(self, entity: IInteractive):
        super().__init__(entity)
