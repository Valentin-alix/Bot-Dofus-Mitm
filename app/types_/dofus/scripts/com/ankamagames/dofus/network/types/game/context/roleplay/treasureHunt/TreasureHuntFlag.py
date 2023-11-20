from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TreasureHuntFlag:
	def __init__(self, mapId:float, state:int):
		self.mapId=mapId
		self.state=state