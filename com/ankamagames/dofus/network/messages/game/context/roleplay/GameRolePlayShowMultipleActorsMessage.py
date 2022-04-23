from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
    


class GameRolePlayShowMultipleActorsMessage(NetworkMessage):
    informationsList:list['GameRolePlayActorInformations']
    

    def init(self, informationsList_:list['GameRolePlayActorInformations']):
        self.informationsList = informationsList_
        
        super().__init__()
    
    