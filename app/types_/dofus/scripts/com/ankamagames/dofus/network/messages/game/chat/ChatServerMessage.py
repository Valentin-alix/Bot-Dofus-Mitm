from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.chat.ChatAbstractServerMessage import ChatAbstractServerMessage
if TYPE_CHECKING:
	...
class ChatServerMessage(ChatAbstractServerMessage):
	def __init__(self, senderId:float, senderName:str, prefix:str, senderAccountId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.senderId=senderId
		self.senderName=senderName
		self.prefix=prefix
		self.senderAccountId=senderAccountId