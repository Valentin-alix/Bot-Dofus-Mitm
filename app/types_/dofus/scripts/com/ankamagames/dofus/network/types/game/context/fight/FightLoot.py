from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightLootObject import FightLootObject
class FightLoot:
	def __init__(self, objects:list[FightLootObject], kamas:int):
		self.objects=objects
		self.kamas=kamas