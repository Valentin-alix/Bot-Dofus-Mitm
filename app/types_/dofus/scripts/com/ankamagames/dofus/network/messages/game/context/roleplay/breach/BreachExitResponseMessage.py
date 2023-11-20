from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class BreachExitResponseMessage:
	def __init__(self, exited:bool):
		self.exited=exited