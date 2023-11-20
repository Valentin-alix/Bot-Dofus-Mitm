from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PresetUseRequestMessage:
	def __init__(self, presetId:int):
		self.presetId=presetId