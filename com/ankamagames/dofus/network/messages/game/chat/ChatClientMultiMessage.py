from com.ankamagames.dofus.network.messages.game.chat.ChatAbstractClientMessage import ChatAbstractClientMessage


class ChatClientMultiMessage(ChatAbstractClientMessage):
    channel:int
    

    def init(self, channel_:int, content_:str):
        self.channel = channel_
        
        super().__init__(content_)
    
    