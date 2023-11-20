from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class SellerBuyerDescriptor:
	def __init__(self, quantities:list[int], types:list[int], taxPercentage:float, taxModificationPercentage:float, maxItemLevel:int, maxItemPerAccount:int, npcContextualId:int, unsoldDelay:int):
		self.quantities=quantities
		self.types=types
		self.taxPercentage=taxPercentage
		self.taxModificationPercentage=taxModificationPercentage
		self.maxItemLevel=maxItemLevel
		self.maxItemPerAccount=maxItemPerAccount
		self.npcContextualId=npcContextualId
		self.unsoldDelay=unsoldDelay