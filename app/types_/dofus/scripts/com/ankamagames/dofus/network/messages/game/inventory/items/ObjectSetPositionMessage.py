from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ObjectSetPositionMessage:
	def __init__(self, objectUID:int, position:int, quantity:int):
		self.objectUID=objectUID
		self.position=position
		self.quantity=quantity