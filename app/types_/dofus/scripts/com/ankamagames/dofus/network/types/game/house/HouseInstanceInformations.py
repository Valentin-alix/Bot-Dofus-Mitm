from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
class HouseInstanceInformations:
	def __init__(self, instanceId:int, ownerTag:AccountTagInformation, price:int):
		self.instanceId=instanceId
		self.ownerTag=ownerTag
		self.price=price