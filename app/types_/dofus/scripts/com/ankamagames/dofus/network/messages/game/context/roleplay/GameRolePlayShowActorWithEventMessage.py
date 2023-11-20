from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.GameRolePlayShowActorMessage import GameRolePlayShowActorMessage
if TYPE_CHECKING:
	...
class GameRolePlayShowActorWithEventMessage(GameRolePlayShowActorMessage):
	def __init__(self, actorEventId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.actorEventId=actorEventId