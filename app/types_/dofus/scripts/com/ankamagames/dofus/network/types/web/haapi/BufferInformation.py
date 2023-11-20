from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class BufferInformation:
	def __init__(self, id:int, amount:int):
		self.id=id
		self.amount=amount