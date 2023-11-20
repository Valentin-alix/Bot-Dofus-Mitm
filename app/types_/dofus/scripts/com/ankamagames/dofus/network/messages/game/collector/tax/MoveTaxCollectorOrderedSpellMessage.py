from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MoveTaxCollectorOrderedSpellMessage:
	def __init__(self, taxCollectorId:float, movedFrom:int, movedTo:int):
		self.taxCollectorId=taxCollectorId
		self.movedFrom=movedFrom
		self.movedTo=movedTo