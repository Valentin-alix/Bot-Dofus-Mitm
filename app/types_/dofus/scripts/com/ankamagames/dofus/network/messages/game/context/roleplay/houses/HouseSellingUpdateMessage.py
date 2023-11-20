from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
class HouseSellingUpdateMessage:
	def __init__(self, houseId:int, instanceId:int, secondHand:bool, realPrice:int, buyerTag:AccountTagInformation):
		self.houseId=houseId
		self.instanceId=instanceId
		self.secondHand=secondHand
		self.realPrice=realPrice
		self.buyerTag=buyerTag