from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class RecycledItem:
	def __init__(self, id:int, qty:int):
		self.id=id
		self.qty=qty