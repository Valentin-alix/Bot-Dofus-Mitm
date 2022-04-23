from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations
    


class AllianceInvitedMessage(NetworkMessage):
    recruterId:int
    recruterName:str
    allianceInfo:'BasicNamedAllianceInformations'
    

    def init(self, recruterId_:int, recruterName_:str, allianceInfo_:'BasicNamedAllianceInformations'):
        self.recruterId = recruterId_
        self.recruterName = recruterName_
        self.allianceInfo = allianceInfo_
        
        super().__init__()
    
    