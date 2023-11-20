from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightResultListEntry import FightResultListEntry
if TYPE_CHECKING:
	...
class FightResultFighterListEntry(FightResultListEntry):
	def __init__(self, id:float, alive:bool, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.id=id
		self.alive=alive