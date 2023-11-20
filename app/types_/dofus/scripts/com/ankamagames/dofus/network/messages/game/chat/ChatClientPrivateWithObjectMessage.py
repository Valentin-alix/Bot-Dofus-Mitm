from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.chat.ChatClientPrivateMessage import ChatClientPrivateMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
class ChatClientPrivateWithObjectMessage(ChatClientPrivateMessage):
	def __init__(self, objects:list[ObjectItem], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.objects=objects