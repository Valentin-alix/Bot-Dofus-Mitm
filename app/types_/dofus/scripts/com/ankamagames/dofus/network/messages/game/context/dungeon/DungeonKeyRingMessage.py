from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class DungeonKeyRingMessage:
	def __init__(self, availables:list[int], unavailables:list[int]):
		self.availables=availables
		self.unavailables=unavailables