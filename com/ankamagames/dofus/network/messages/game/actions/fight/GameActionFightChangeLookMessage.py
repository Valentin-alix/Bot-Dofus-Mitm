from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class GameActionFightChangeLookMessage(AbstractGameActionMessage):
    targetId:int
    entityLook:'EntityLook'
    

    def init(self, targetId_:int, entityLook_:'EntityLook', actionId_:int, sourceId_:int):
        self.targetId = targetId_
        self.entityLook = entityLook_
        
        super().__init__(actionId_, sourceId_)
    
    