from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MoveTaxCollectorPresetSpellMessage:
	def __init__(self, presetId:int, movedFrom:int, movedTo:int):
		self.presetId=presetId
		self.movedFrom=movedFrom
		self.movedTo=movedTo