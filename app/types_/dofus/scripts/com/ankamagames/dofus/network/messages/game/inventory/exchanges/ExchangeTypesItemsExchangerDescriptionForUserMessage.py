from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.BidExchangerObjectInfo import BidExchangerObjectInfo
class ExchangeTypesItemsExchangerDescriptionForUserMessage:
	def __init__(self, objectGID:int, objectType:int, itemTypeDescriptions:list[BidExchangerObjectInfo]):
		self.objectGID=objectGID
		self.objectType=objectType
		self.itemTypeDescriptions=itemTypeDescriptions