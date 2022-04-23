from com.ankamagames.dofus.network.messages.game.chat.ChatAbstractServerMessage import ChatAbstractServerMessage


class ChatServerMessage(ChatAbstractServerMessage):
    senderId:int
    senderName:str
    prefix:str
    senderAccountId:int
    

    def init(self, senderId_:int, senderName_:str, prefix_:str, senderAccountId_:int, channel_:int, content_:str, timestamp_:int, fingerprint_:str):
        self.senderId = senderId_
        self.senderName = senderName_
        self.prefix = prefix_
        self.senderAccountId = senderAccountId_
        
        super().__init__(channel_, content_, timestamp_, fingerprint_)
    
    