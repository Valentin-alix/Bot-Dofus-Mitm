from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ConsoleMessage:
	def __init__(self, type:int, content:str):
		self.type=type
		self.content=content