from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
class IdentificationSuccessMessage:
	def __init__(self, login:str, accountTag:AccountTagInformation, accountId:int, communityId:int, accountCreation:float, subscriptionEndDate:float, havenbagAvailableRoom:int):
		self.login=login
		self.accountTag=accountTag
		self.accountId=accountId
		self.communityId=communityId
		self.accountCreation=accountCreation
		self.subscriptionEndDate=subscriptionEndDate
		self.havenbagAvailableRoom=havenbagAvailableRoom