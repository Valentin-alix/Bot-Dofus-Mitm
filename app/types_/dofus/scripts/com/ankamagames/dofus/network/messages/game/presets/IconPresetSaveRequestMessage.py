from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class IconPresetSaveRequestMessage:
	def __init__(self, presetId:int, symbolId:int, updateData:bool):
		self.presetId=presetId
		self.symbolId=symbolId
		self.updateData=updateData