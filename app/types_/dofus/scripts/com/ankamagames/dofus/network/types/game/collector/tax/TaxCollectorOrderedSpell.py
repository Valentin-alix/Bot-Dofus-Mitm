from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TaxCollectorOrderedSpell:
	def __init__(self, spellId:int, slot:int):
		self.spellId=spellId
		self.slot=slot