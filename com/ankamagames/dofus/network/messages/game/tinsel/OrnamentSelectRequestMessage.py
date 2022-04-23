from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class OrnamentSelectRequestMessage(NetworkMessage):
    ornamentId:int
    

    def init(self, ornamentId_:int):
        self.ornamentId = ornamentId_
        
        super().__init__()
    
    