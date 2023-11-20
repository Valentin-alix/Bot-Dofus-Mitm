from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class BreachReward:
	def __init__(self, id:int, buyLocks:list[int], buyCriterion:str, remainingQty:int, price:int):
		self.id=id
		self.buyLocks=buyLocks
		self.buyCriterion=buyCriterion
		self.remainingQty=remainingQty
		self.price=price