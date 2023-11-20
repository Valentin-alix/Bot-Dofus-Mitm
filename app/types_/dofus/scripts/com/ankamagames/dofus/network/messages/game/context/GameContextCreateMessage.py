from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameContextCreateMessage:
	def __init__(self, context:int):
		self.context=context