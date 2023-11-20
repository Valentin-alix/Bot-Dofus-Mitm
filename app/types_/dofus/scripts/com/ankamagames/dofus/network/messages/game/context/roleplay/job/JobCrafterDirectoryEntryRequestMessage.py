from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class JobCrafterDirectoryEntryRequestMessage:
	def __init__(self, playerId:int):
		self.playerId=playerId