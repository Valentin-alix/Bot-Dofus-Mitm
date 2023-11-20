from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectCreature import ObjectEffectCreature
if TYPE_CHECKING:
	...
class ObjectEffectLadder(ObjectEffectCreature):
	def __init__(self, monsterCount:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.monsterCount=monsterCount