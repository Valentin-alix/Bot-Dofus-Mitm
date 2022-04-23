from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class GuildApplicationIsAnsweredMessage(NetworkMessage):
    accepted:bool
    guildInformation:'GuildInformations'
    

    def init(self, accepted_:bool, guildInformation_:'GuildInformations'):
        self.accepted = accepted_
        self.guildInformation = guildInformation_
        
        super().__init__()
    
    