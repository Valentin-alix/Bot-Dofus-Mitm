from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayDelayedActionFinishedMessage:
	def __init__(self, delayedCharacterId:float, delayTypeId:int):
		self.delayedCharacterId=delayedCharacterId
		self.delayTypeId=delayTypeId