from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ShortcutBarSwapRequestMessage:
	def __init__(self, barType:int, firstSlot:int, secondSlot:int):
		self.barType=barType
		self.firstSlot=firstSlot
		self.secondSlot=secondSlot