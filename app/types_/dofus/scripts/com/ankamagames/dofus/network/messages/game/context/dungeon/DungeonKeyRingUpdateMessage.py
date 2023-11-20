from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class DungeonKeyRingUpdateMessage:
	def __init__(self, dungeonId:int, available:bool):
		self.dungeonId=dungeonId
		self.available=available