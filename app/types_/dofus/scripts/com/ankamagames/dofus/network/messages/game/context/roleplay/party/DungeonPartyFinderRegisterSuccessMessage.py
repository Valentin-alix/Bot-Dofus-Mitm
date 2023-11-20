from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class DungeonPartyFinderRegisterSuccessMessage:
	def __init__(self, dungeonIds:list[int]):
		self.dungeonIds=dungeonIds