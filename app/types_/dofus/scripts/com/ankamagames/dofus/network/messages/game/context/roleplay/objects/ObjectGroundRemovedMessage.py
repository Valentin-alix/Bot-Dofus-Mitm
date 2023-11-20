from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ObjectGroundRemovedMessage:
	def __init__(self, cell:int):
		self.cell=cell