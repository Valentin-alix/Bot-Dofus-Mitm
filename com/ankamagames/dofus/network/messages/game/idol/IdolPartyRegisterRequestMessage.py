from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class IdolPartyRegisterRequestMessage(NetworkMessage):
    register:bool
    

    def init(self, register_:bool):
        self.register = register_
        
        super().__init__()
    
    