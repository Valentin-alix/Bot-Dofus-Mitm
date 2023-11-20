from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.SellerBuyerDescriptor import SellerBuyerDescriptor
class ExchangeStartedBidBuyerMessage:
	def __init__(self, buyerDescriptor:SellerBuyerDescriptor):
		self.buyerDescriptor=buyerDescriptor