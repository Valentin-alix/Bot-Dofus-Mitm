from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BasicAckMessage(NetworkMessage):
    seq:int
    lastPacketId:int
    

    def init(self, seq_:int, lastPacketId_:int):
        self.seq = seq_
        self.lastPacketId = lastPacketId_
        
        super().__init__()
    
    