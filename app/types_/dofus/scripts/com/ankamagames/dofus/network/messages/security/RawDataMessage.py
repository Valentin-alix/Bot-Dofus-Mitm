from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class RawDataMessage:
	def __init__(self, content:int):
		self.content=content