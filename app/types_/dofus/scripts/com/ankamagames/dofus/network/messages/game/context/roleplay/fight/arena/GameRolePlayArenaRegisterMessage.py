from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayArenaRegisterMessage:
	def __init__(self, battleMode:int):
		self.battleMode=battleMode