from com.ankamagames.dofus.network.messages.game.chat.ChatAbstractServerMessage import ChatAbstractServerMessage


class ChatServerCopyMessage(ChatAbstractServerMessage):
    receiverId:int
    receiverName:str
    

    def init(self, receiverId_:int, receiverName_:str, channel_:int, content_:str, timestamp_:int, fingerprint_:str):
        self.receiverId = receiverId_
        self.receiverName = receiverName_
        
        super().__init__(channel_, content_, timestamp_, fingerprint_)
    
    