from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightLoot import FightLoot
class FightResultListEntry:
	def __init__(self, outcome:int, wave:int, rewards:FightLoot):
		self.outcome=outcome
		self.wave=wave
		self.rewards=rewards