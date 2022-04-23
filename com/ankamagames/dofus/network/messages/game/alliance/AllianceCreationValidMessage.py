from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class AllianceCreationValidMessage(NetworkMessage):
    allianceName:str
    allianceTag:str
    allianceEmblem:'GuildEmblem'
    

    def init(self, allianceName_:str, allianceTag_:str, allianceEmblem_:'GuildEmblem'):
        self.allianceName = allianceName_
        self.allianceTag = allianceTag_
        self.allianceEmblem = allianceEmblem_
        
        super().__init__()
    
    