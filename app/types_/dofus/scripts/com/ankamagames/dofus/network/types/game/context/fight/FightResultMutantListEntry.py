from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightResultFighterListEntry import FightResultFighterListEntry
if TYPE_CHECKING:
	...
class FightResultMutantListEntry(FightResultFighterListEntry):
	def __init__(self, level:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.level=level