from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SymbioticObjectAssociatedMessage(NetworkMessage):
    hostUID:int
    

    def init(self, hostUID_:int):
        self.hostUID = hostUID_
        
        super().__init__()
    
    