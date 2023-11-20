from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class BreachRoomUnlockResultMessage:
	def __init__(self, roomId:int, result:int):
		self.roomId=roomId
		self.result=result