from com.ankamagames.dofus.network.messages.game.chat.ChatServerMessage import ChatServerMessage


class ChatAdminServerMessage(ChatServerMessage):
    

    def init(self, senderId_:int, senderName_:str, prefix_:str, senderAccountId_:int, channel_:int, content_:str, timestamp_:int, fingerprint_:str):
        
        super().__init__(senderId_, senderName_, prefix_, senderAccountId_, channel_, content_, timestamp_, fingerprint_)
    
    