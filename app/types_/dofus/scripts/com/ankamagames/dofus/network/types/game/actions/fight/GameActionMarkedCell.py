from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameActionMarkedCell:
	def __init__(self, cellId:int, zoneSize:int, cellColor:int, cellsType:int):
		self.cellId=cellId
		self.zoneSize=zoneSize
		self.cellColor=cellColor
		self.cellsType=cellsType