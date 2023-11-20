from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.chat.ChatClientMultiMessage import ChatClientMultiMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
class ChatClientMultiWithObjectMessage(ChatClientMultiMessage):
	def __init__(self, objects:list[ObjectItem], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.objects=objects