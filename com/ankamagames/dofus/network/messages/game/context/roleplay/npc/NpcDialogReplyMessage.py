from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NpcDialogReplyMessage(NetworkMessage):
    replyId:int
    

    def init(self, replyId_:int):
        self.replyId = replyId_
        
        super().__init__()
    
    