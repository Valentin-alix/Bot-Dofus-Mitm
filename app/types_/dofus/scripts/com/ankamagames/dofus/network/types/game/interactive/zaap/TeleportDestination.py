from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TeleportDestination:
	def __init__(self, type:int, mapId:float, subAreaId:int, level:int, cost:int):
		self.type=type
		self.mapId=mapId
		self.subAreaId=subAreaId
		self.level=level
		self.cost=cost