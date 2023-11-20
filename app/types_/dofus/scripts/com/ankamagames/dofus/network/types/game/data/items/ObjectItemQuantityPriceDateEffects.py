from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItemGenericQuantity import ObjectItemGenericQuantity
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectEffects import ObjectEffects
class ObjectItemQuantityPriceDateEffects(ObjectItemGenericQuantity):
	def __init__(self, price:int, effects:ObjectEffects, date:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.price=price
		self.effects=effects
		self.date=date