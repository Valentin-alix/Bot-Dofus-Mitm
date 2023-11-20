from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.delay.GameRolePlayDelayedActionMessage import GameRolePlayDelayedActionMessage
if TYPE_CHECKING:
	...
class GameRolePlayDelayedObjectUseMessage(GameRolePlayDelayedActionMessage):
	def __init__(self, objectGID:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.objectGID=objectGID