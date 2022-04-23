from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.GameContextActorPositionInformations import GameContextActorPositionInformations
    


class GameContextBasicSpawnInformation(NetworkMessage):
    teamId:int
    alive:bool
    informations:'GameContextActorPositionInformations'
    

    def init(self, teamId_:int, alive_:bool, informations_:'GameContextActorPositionInformations'):
        self.teamId = teamId_
        self.alive = alive_
        self.informations = informations_
        
        super().__init__()
    
    