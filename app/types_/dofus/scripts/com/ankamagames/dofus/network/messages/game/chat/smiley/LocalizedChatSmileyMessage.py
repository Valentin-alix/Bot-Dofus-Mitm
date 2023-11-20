from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.chat.smiley.ChatSmileyMessage import ChatSmileyMessage
if TYPE_CHECKING:
	...
class LocalizedChatSmileyMessage(ChatSmileyMessage):
	def __init__(self, cellId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.cellId=cellId