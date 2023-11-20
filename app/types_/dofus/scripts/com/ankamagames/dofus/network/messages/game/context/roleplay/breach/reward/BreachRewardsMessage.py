from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachReward import BreachReward
class BreachRewardsMessage:
	def __init__(self, rewards:list[BreachReward]):
		self.rewards=rewards