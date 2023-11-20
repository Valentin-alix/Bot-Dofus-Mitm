from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AreaFightModificatorUpdateMessage:
	def __init__(self, spellPairId:int):
		self.spellPairId=spellPairId