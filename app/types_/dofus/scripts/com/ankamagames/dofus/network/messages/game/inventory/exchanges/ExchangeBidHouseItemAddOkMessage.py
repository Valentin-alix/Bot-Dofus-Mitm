from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInBid import ObjectItemToSellInBid
class ExchangeBidHouseItemAddOkMessage:
	def __init__(self, itemInfo:ObjectItemToSellInBid):
		self.itemInfo=itemInfo