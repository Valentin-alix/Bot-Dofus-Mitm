from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class BasicStatMessage:
	def __init__(self, timeSpent:float, statId:int):
		self.timeSpent=timeSpent
		self.statId=statId