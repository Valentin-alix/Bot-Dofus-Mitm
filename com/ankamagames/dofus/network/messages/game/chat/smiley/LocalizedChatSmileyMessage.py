from com.ankamagames.dofus.network.messages.game.chat.smiley.ChatSmileyMessage import ChatSmileyMessage


class LocalizedChatSmileyMessage(ChatSmileyMessage):
    cellId:int
    

    def init(self, cellId_:int, entityId_:int, smileyId_:int, accountId_:int):
        self.cellId = cellId_
        
        super().__init__(entityId_, smileyId_, accountId_)
    
    