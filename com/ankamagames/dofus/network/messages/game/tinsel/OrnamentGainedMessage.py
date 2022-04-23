from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class OrnamentGainedMessage(NetworkMessage):
    ornamentId:int
    

    def init(self, ornamentId_:int):
        self.ornamentId = ornamentId_
        
        super().__init__()
    
    