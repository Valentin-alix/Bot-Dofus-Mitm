from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItemGenericQuantity import ObjectItemGenericQuantity
class ExchangeBidHouseUnsoldItemsMessage:
	def __init__(self, items:list[ObjectItemGenericQuantity]):
		self.items=items