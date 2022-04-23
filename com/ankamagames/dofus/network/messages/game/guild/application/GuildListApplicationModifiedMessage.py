from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.application.GuildApplicationInformation import GuildApplicationInformation
    


class GuildListApplicationModifiedMessage(NetworkMessage):
    apply:'GuildApplicationInformation'
    state:int
    playerId:int
    

    def init(self, apply_:'GuildApplicationInformation', state_:int, playerId_:int):
        self.apply = apply_
        self.state = state_
        self.playerId = playerId_
        
        super().__init__()
    
    