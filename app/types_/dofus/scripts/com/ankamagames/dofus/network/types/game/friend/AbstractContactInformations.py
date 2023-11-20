from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
class AbstractContactInformations:
	def __init__(self, accountId:int, accountTag:AccountTagInformation):
		self.accountId=accountId
		self.accountTag=accountTag