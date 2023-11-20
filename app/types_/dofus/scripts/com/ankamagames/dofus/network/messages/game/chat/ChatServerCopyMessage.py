from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.chat.ChatAbstractServerMessage import ChatAbstractServerMessage
if TYPE_CHECKING:
	...
class ChatServerCopyMessage(ChatAbstractServerMessage):
	def __init__(self, receiverId:int, receiverName:str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.receiverId=receiverId
		self.receiverName=receiverName