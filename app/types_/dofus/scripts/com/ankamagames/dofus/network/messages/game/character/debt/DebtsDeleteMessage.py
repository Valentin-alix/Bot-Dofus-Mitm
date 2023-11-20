from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class DebtsDeleteMessage:
	def __init__(self, reason:int, debts:list[float]):
		self.reason=reason
		self.debts=debts