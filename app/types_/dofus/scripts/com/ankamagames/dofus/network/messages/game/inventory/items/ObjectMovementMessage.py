from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ObjectMovementMessage:
	def __init__(self, objectUID:int, position:int):
		self.objectUID=objectUID
		self.position=position