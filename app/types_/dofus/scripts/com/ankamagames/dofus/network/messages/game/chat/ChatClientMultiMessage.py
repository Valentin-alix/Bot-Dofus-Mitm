from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.chat.ChatAbstractClientMessage import ChatAbstractClientMessage
if TYPE_CHECKING:
	...
class ChatClientMultiMessage(ChatAbstractClientMessage):
	def __init__(self, channel:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.channel=channel