from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SequenceEndMessage(NetworkMessage):
    actionId:int
    authorId:int
    sequenceType:int
    

    def init(self, actionId_:int, authorId_:int, sequenceType_:int):
        self.actionId = actionId_
        self.authorId = authorId_
        self.sequenceType = sequenceType_
        
        super().__init__()
    
    