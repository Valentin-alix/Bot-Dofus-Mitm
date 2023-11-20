from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnStartMessage import GameFightTurnStartMessage
if TYPE_CHECKING:
	...
class GameFightTurnResumeMessage(GameFightTurnStartMessage):
	def __init__(self, remainingTime:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.remainingTime=remainingTime