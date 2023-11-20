from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class RemoveTaxCollectorPresetSpellMessage:
	def __init__(self, presetId:int, slot:int):
		self.presetId=presetId
		self.slot=slot