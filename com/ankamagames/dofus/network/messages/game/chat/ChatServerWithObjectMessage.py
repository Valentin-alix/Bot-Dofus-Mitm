from com.ankamagames.dofus.network.messages.game.chat.ChatServerMessage import ChatServerMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    


class ChatServerWithObjectMessage(ChatServerMessage):
    objects:list['ObjectItem']
    

    def init(self, objects_:list['ObjectItem'], senderId_:int, senderName_:str, prefix_:str, senderAccountId_:int, channel_:int, content_:str, timestamp_:int, fingerprint_:str):
        self.objects = objects_
        
        super().__init__(senderId_, senderName_, prefix_, senderAccountId_, channel_, content_, timestamp_, fingerprint_)
    
    