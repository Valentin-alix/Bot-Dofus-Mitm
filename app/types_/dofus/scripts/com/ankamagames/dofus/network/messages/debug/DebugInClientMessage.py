from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class DebugInClientMessage:
	def __init__(self, level:int, message:str):
		self.level=level
		self.message=message