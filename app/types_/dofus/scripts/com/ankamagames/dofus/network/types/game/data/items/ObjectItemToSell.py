from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.Item import Item
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
class ObjectItemToSell(Item):
	def __init__(self, objectGID:int, effects:list[ObjectEffect], objectUID:int, quantity:int, objectPrice:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.objectGID=objectGID
		self.effects=effects
		self.objectUID=objectUID
		self.quantity=quantity
		self.objectPrice=objectPrice