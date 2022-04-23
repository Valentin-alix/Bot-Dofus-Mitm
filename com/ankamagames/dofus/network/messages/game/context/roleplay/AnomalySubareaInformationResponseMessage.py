from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.AnomalySubareaInformation import AnomalySubareaInformation
    


class AnomalySubareaInformationResponseMessage(NetworkMessage):
    subareas:list['AnomalySubareaInformation']
    

    def init(self, subareas_:list['AnomalySubareaInformation']):
        self.subareas = subareas_
        
        super().__init__()
    
    