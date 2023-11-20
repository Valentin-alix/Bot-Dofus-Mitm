from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayDelayedActionMessage:
	def __init__(self, delayedCharacterId:float, delayTypeId:int, delayEndTime:float):
		self.delayedCharacterId=delayedCharacterId
		self.delayTypeId=delayTypeId
		self.delayEndTime=delayEndTime