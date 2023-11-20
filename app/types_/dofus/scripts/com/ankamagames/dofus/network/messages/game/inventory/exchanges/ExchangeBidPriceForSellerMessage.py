from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidPriceMessage import ExchangeBidPriceMessage
if TYPE_CHECKING:
	...
class ExchangeBidPriceForSellerMessage(ExchangeBidPriceMessage):
	def __init__(self, allIdentical:bool, minimalPrices:list[int], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.allIdentical=allIdentical
		self.minimalPrices=minimalPrices