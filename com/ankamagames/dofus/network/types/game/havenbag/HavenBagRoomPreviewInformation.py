from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HavenBagRoomPreviewInformation(NetworkMessage):
    roomId:int
    themeId:int
    

    def init(self, roomId_:int, themeId_:int):
        self.roomId = roomId_
        self.themeId = themeId_
        
        super().__init__()
    
    