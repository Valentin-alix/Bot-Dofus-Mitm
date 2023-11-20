from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightLifePointsLostMessage import GameActionFightLifePointsLostMessage
if TYPE_CHECKING:
	...
class GameActionFightLifeAndShieldPointsLostMessage(GameActionFightLifePointsLostMessage):
	def __init__(self, shieldLoss:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.shieldLoss=shieldLoss