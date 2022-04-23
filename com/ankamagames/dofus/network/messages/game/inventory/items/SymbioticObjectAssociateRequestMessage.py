from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SymbioticObjectAssociateRequestMessage(NetworkMessage):
    symbioteUID:int
    symbiotePos:int
    hostUID:int
    hostPos:int
    

    def init(self, symbioteUID_:int, symbiotePos_:int, hostUID_:int, hostPos_:int):
        self.symbioteUID = symbioteUID_
        self.symbiotePos = symbiotePos_
        self.hostUID = hostUID_
        self.hostPos = hostPos_
        
        super().__init__()
    
    