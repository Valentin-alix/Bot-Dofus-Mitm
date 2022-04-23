from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class OrnamentLostMessage(NetworkMessage):
    ornamentId:int
    

    def init(self, ornamentId_:int):
        self.ornamentId = ornamentId_
        
        super().__init__()
    
    