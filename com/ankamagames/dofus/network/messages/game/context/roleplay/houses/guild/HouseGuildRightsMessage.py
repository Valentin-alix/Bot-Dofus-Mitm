from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class HouseGuildRightsMessage(NetworkMessage):
    houseId:int
    instanceId:int
    secondHand:bool
    guildInfo:'GuildInformations'
    rights:int
    

    def init(self, houseId_:int, instanceId_:int, secondHand_:bool, guildInfo_:'GuildInformations', rights_:int):
        self.houseId = houseId_
        self.instanceId = instanceId_
        self.secondHand = secondHand_
        self.guildInfo = guildInfo_
        self.rights = rights_
        
        super().__init__()
    
    