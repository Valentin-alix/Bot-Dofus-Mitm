from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightResultFighterListEntry import FightResultFighterListEntry
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightResultAdditionalData import FightResultAdditionalData
class FightResultPlayerListEntry(FightResultFighterListEntry):
	def __init__(self, level:int, additional:list[FightResultAdditionalData], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.level=level
		self.additional=additional