from com.ankamagames.dofus.network.messages.game.chat.ChatClientMultiMessage import ChatClientMultiMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    


class ChatClientMultiWithObjectMessage(ChatClientMultiMessage):
    objects:list['ObjectItem']
    

    def init(self, objects_:list['ObjectItem'], channel_:int, content_:str):
        self.objects = objects_
        
        super().__init__(channel_, content_)
    
    