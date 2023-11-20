from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class InventoryWeightMessage:
	def __init__(self, inventoryWeight:int, weightMax:int):
		self.inventoryWeight=inventoryWeight
		self.weightMax=weightMax