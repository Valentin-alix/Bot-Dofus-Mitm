from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class CheckIntegrityMessage:
	def __init__(self, data:list[int]):
		self.data=data