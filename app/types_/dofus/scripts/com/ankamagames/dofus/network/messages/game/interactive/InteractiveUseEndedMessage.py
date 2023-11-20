from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class InteractiveUseEndedMessage:
	def __init__(self, elemId:int, skillId:int):
		self.elemId=elemId
		self.skillId=skillId