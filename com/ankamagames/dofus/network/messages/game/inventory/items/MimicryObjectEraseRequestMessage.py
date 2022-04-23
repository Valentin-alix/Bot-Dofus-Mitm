from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MimicryObjectEraseRequestMessage(NetworkMessage):
    hostUID:int
    hostPos:int
    

    def init(self, hostUID_:int, hostPos_:int):
        self.hostUID = hostUID_
        self.hostPos = hostPos_
        
        super().__init__()
    
    