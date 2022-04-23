from com.ankamagames.dofus.network.messages.game.chat.ChatAbstractClientMessage import ChatAbstractClientMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
    


class ChatClientPrivateMessage(ChatAbstractClientMessage):
    receiver:'AbstractPlayerSearchInformation'
    

    def init(self, receiver_:'AbstractPlayerSearchInformation', content_:str):
        self.receiver = receiver_
        
        super().__init__(content_)
    
    