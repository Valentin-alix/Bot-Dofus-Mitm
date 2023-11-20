from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSell import ObjectItemToSell
if TYPE_CHECKING:
	...
class ObjectItemToSellInBid(ObjectItemToSell):
	def __init__(self, unsoldDelay:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.unsoldDelay=unsoldDelay