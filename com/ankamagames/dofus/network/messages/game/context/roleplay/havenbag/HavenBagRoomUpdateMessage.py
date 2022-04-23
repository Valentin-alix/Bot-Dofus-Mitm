from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.havenbag.HavenBagRoomPreviewInformation import HavenBagRoomPreviewInformation
    


class HavenBagRoomUpdateMessage(NetworkMessage):
    action:int
    roomsPreview:list['HavenBagRoomPreviewInformation']
    

    def init(self, action_:int, roomsPreview_:list['HavenBagRoomPreviewInformation']):
        self.action = action_
        self.roomsPreview = roomsPreview_
        
        super().__init__()
    
    