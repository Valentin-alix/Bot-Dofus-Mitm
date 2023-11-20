from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TeleportOnSameMapMessage:
	def __init__(self, targetId:float, cellId:int):
		self.targetId=targetId
		self.cellId=cellId