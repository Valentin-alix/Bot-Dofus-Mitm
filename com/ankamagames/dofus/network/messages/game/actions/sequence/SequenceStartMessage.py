from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SequenceStartMessage(NetworkMessage):
    sequenceType:int
    authorId:int
    

    def init(self, sequenceType_:int, authorId_:int):
        self.sequenceType = sequenceType_
        self.authorId = authorId_
        
        super().__init__()
    
    