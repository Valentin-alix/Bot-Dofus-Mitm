from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameActionSpamMessage:
	def __init__(self, cells:list[int]):
		self.cells=cells