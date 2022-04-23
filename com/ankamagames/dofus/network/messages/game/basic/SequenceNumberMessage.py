from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SequenceNumberMessage(NetworkMessage):
    number:int
    

    def init(self, number_:int):
        self.number = number_
        
        super().__init__()
    
    