from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.emote.EmotePlayAbstractMessage import EmotePlayAbstractMessage
if TYPE_CHECKING:
	...
class EmotePlayMessage(EmotePlayAbstractMessage):
	def __init__(self, actorId:float, accountId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.actorId=actorId
		self.accountId=accountId