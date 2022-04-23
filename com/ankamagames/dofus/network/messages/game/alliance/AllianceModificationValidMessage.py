from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class AllianceModificationValidMessage(NetworkMessage):
    allianceName:str
    allianceTag:str
    Alliancemblem:'GuildEmblem'
    

    def init(self, allianceName_:str, allianceTag_:str, Alliancemblem_:'GuildEmblem'):
        self.allianceName = allianceName_
        self.allianceTag = allianceTag_
        self.Alliancemblem = Alliancemblem_
        
        super().__init__()
    
    