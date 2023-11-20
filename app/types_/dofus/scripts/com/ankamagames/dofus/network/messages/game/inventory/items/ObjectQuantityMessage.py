from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ObjectQuantityMessage:
	def __init__(self, objectUID:int, quantity:int, origin:int):
		self.objectUID=objectUID
		self.quantity=quantity
		self.origin=origin