from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations
    


class AllianceJoinedMessage(NetworkMessage):
    allianceInfo:'AllianceInformations'
    enabled:bool
    leadingGuildId:int
    

    def init(self, allianceInfo_:'AllianceInformations', enabled_:bool, leadingGuildId_:int):
        self.allianceInfo = allianceInfo_
        self.enabled = enabled_
        self.leadingGuildId = leadingGuildId_
        
        super().__init__()
    
    