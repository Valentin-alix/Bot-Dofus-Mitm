from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HouseInformations:
	def __init__(self, houseId:int, modelId:int):
		self.houseId=houseId
		self.modelId=modelId