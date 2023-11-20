from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameActionFightCastRequestMessage:
	def __init__(self, spellId:int, cellId:int):
		self.spellId=spellId
		self.cellId=cellId