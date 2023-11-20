from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayPlayerFightRequestMessage:
	def __init__(self, targetId:int, targetCellId:int, friendly:bool):
		self.targetId=targetId
		self.targetCellId=targetCellId
		self.friendly=friendly