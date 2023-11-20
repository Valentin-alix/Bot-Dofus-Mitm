from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class SequenceNumberMessage:
	def __init__(self, number:int):
		self.number=number