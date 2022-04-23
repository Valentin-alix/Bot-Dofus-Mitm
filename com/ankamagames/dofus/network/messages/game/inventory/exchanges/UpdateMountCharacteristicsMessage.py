from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.mount.UpdateMountCharacteristic import UpdateMountCharacteristic
    


class UpdateMountCharacteristicsMessage(NetworkMessage):
    rideId:int
    boostToUpdateList:list['UpdateMountCharacteristic']
    

    def init(self, rideId_:int, boostToUpdateList_:list['UpdateMountCharacteristic']):
        self.rideId = rideId_
        self.boostToUpdateList = boostToUpdateList_
        
        super().__init__()
    
    