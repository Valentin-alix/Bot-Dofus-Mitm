from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class BreachKickRequestMessage:
	def __init__(self, target:int):
		self.target=target