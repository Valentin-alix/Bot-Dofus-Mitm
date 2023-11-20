from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayArenaPlayerBehavioursMessage:
	def __init__(self, flags:list[str], sanctions:list[str], banDuration:int):
		self.flags=flags
		self.sanctions=sanctions
		self.banDuration=banDuration