from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class BreachRewardBoughtMessage:
	def __init__(self, id:int, bought:bool):
		self.id=id
		self.bought=bought