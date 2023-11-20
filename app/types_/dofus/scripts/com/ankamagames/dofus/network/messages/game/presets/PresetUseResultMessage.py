from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PresetUseResultMessage:
	def __init__(self, presetId:int, code:int):
		self.presetId=presetId
		self.code=code