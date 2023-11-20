from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class DungeonPartyFinderListenRequestMessage:
	def __init__(self, dungeonId:int):
		self.dungeonId=dungeonId