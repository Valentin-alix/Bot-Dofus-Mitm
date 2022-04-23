from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NpcDialogQuestionMessage(NetworkMessage):
    messageId:int
    dialogParams:list[str]
    visibleReplies:list[int]
    

    def init(self, messageId_:int, dialogParams_:list[str], visibleReplies_:list[int]):
        self.messageId = messageId_
        self.dialogParams = dialogParams_
        self.visibleReplies = visibleReplies_
        
        super().__init__()
    
    