from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DocumentReadingBeginMessage(NetworkMessage):
    documentId:int
    

    def init(self, documentId_:int):
        self.documentId = documentId_
        
        super().__init__()
    
    