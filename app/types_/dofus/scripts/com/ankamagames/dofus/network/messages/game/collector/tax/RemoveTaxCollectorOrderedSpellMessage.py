from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class RemoveTaxCollectorOrderedSpellMessage:
	def __init__(self, taxCollectorId:float, slot:int):
		self.taxCollectorId=taxCollectorId
		self.slot=slot