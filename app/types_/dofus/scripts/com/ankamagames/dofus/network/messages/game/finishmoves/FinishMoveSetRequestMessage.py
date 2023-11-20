from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class FinishMoveSetRequestMessage:
	def __init__(self, finishMoveId:int, finishMoveState:bool):
		self.finishMoveId=finishMoveId
		self.finishMoveState=finishMoveState