from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger
class ObjectEffectMount(ObjectEffect):
	def __init__(self, id:int, expirationDate:int, model:int, name:str, owner:str, level:int, reproductionCount:int, reproductionCountMax:int, effects:list[ObjectEffectInteger], capacities:list[int], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.id=id
		self.expirationDate=expirationDate
		self.model=model
		self.name=name
		self.owner=owner
		self.level=level
		self.reproductionCount=reproductionCount
		self.reproductionCountMax=reproductionCountMax
		self.effects=effects
		self.capacities=capacities