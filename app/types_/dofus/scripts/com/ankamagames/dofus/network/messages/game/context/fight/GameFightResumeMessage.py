from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.fight.GameFightSpectateMessage import GameFightSpectateMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightSpellCooldown import GameFightSpellCooldown
class GameFightResumeMessage(GameFightSpectateMessage):
	def __init__(self, spellCooldowns:list[GameFightSpellCooldown], summonCount:int, bombCount:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.spellCooldowns=spellCooldowns
		self.summonCount=summonCount
		self.bombCount=bombCount