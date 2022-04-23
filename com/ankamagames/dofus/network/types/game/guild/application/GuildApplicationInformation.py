from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.application.ApplicationPlayerInformation import ApplicationPlayerInformation
    


class GuildApplicationInformation(NetworkMessage):
    playerInfo:'ApplicationPlayerInformation'
    applyText:str
    creationDate:int
    

    def init(self, playerInfo_:'ApplicationPlayerInformation', applyText_:str, creationDate_:int):
        self.playerInfo = playerInfo_
        self.applyText = applyText_
        self.creationDate = creationDate_
        
        super().__init__()
    
    