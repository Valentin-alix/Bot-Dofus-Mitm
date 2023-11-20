from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.character.stats.UpdateLifePointsMessage import UpdateLifePointsMessage
if TYPE_CHECKING:
	...
class LifePointsRegenEndMessage(UpdateLifePointsMessage):
	def __init__(self, lifePointsGained:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.lifePointsGained=lifePointsGained