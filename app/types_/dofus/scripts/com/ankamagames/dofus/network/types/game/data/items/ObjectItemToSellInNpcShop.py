from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItemMinimalInformation import ObjectItemMinimalInformation
if TYPE_CHECKING:
	...
class ObjectItemToSellInNpcShop(ObjectItemMinimalInformation):
	def __init__(self, objectPrice:int, buyCriterion:str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.objectPrice=objectPrice
		self.buyCriterion=buyCriterion