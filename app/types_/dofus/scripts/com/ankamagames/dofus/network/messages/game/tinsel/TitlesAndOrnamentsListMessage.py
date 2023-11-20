from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TitlesAndOrnamentsListMessage:
	def __init__(self, titles:list[int], ornaments:list[int], activeTitle:int, activeOrnament:int):
		self.titles=titles
		self.ornaments=ornaments
		self.activeTitle=activeTitle
		self.activeOrnament=activeOrnament