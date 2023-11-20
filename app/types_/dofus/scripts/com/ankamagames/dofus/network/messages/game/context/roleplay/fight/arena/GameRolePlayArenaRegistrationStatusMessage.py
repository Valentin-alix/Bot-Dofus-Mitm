from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayArenaRegistrationStatusMessage:
	def __init__(self, registered:bool, step:int, battleMode:int):
		self.registered=registered
		self.step=step
		self.battleMode=battleMode