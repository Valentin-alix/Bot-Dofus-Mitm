from com.ankamagames.dofus.network.messages.game.chat.ChatClientPrivateMessage import ChatClientPrivateMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
    


class ChatClientPrivateWithObjectMessage(ChatClientPrivateMessage):
    objects:list['ObjectItem']
    

    def init(self, objects_:list['ObjectItem'], receiver_:'AbstractPlayerSearchInformation', content_:str):
        self.objects = objects_
        
        super().__init__(receiver_, content_)
    
    