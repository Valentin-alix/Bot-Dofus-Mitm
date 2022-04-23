from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.restriction.ActorRestrictionsInformations import ActorRestrictionsInformations
    


class SetCharacterRestrictionsMessage(NetworkMessage):
    actorId:int
    restrictions:'ActorRestrictionsInformations'
    

    def init(self, actorId_:int, restrictions_:'ActorRestrictionsInformations'):
        self.actorId = actorId_
        self.restrictions = restrictions_
        
        super().__init__()
    
    