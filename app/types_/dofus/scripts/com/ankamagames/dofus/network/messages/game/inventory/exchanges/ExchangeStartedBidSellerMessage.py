from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.SellerBuyerDescriptor import SellerBuyerDescriptor
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInBid import ObjectItemToSellInBid
class ExchangeStartedBidSellerMessage:
	def __init__(self, sellerDescriptor:SellerBuyerDescriptor, objectsInfos:list[ObjectItemToSellInBid]):
		self.sellerDescriptor=sellerDescriptor
		self.objectsInfos=objectsInfos