from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class BreachBudgetMessage:
	def __init__(self, bugdet:int):
		self.bugdet=bugdet