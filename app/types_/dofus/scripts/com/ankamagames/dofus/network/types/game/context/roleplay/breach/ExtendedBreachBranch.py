from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachBranch import BreachBranch
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachReward import BreachReward
class ExtendedBreachBranch(BreachBranch):
	def __init__(self, rewards:list[BreachReward], modifier:int, prize:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.rewards=rewards
		self.modifier=modifier
		self.prize=prize