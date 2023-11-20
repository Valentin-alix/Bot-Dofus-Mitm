from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ItemDurability:
	def __init__(self, durability:int, durabilityMax:int):
		self.durability=durability
		self.durabilityMax=durabilityMax