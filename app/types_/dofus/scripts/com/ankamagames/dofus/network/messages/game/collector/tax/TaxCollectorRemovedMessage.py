from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TaxCollectorRemovedMessage:
	def __init__(self, collectorId:float):
		self.collectorId=collectorId