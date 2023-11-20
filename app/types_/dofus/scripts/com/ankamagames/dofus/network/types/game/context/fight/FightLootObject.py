from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class FightLootObject:
	def __init__(self, objectId:int, quantity:int, priorityHint:int):
		self.objectId=objectId
		self.quantity=quantity
		self.priorityHint=priorityHint