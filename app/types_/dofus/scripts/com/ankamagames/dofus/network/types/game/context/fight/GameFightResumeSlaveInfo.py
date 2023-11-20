from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightSpellCooldown import GameFightSpellCooldown
class GameFightResumeSlaveInfo:
	def __init__(self, slaveId:float, spellCooldowns:list[GameFightSpellCooldown], summonCount:int, bombCount:int):
		self.slaveId=slaveId
		self.spellCooldowns=spellCooldowns
		self.summonCount=summonCount
		self.bombCount=bombCount