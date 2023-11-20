from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ShortcutBarRemovedMessage:
	def __init__(self, barType:int, slot:int):
		self.barType=barType
		self.slot=slot