from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TaxCollectorHarvestedMessage:
	def __init__(self, taxCollectorId:float, harvesterId:int, harvesterName:str):
		self.taxCollectorId=taxCollectorId
		self.harvesterId=harvesterId
		self.harvesterName=harvesterName