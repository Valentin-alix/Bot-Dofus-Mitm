from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AdditionalTaxCollectorInformation:
	def __init__(self, collectorCallerId:int, collectorCallerName:str, date:int):
		self.collectorCallerId=collectorCallerId
		self.collectorCallerName=collectorCallerName
		self.date=date