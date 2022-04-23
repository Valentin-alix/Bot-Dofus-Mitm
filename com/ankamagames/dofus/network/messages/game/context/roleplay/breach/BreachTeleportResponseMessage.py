from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachTeleportResponseMessage(NetworkMessage):
    teleported:bool
    

    def init(self, teleported_:bool):
        self.teleported = teleported_
        
        super().__init__()
    
    