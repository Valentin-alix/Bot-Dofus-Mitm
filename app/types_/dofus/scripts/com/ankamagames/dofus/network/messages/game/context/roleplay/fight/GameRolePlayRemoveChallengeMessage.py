from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayRemoveChallengeMessage:
	def __init__(self, fightId:int):
		self.fightId=fightId