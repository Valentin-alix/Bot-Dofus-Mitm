from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MapFightCountMessage:
	def __init__(self, fightCount:int):
		self.fightCount=fightCount