from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class InteractiveUsedMessage:
	def __init__(self, entityId:int, elemId:int, skillId:int, duration:int, canMove:bool):
		self.entityId=entityId
		self.elemId=elemId
		self.skillId=skillId
		self.duration=duration
		self.canMove=canMove