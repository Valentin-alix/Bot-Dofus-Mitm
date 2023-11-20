from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayFightRequestCanceledMessage:
	def __init__(self, fightId:int, sourceId:float, targetId:float):
		self.fightId=fightId
		self.sourceId=sourceId
		self.targetId=targetId