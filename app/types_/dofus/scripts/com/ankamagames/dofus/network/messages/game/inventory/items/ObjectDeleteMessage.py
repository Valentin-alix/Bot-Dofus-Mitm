from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ObjectDeleteMessage:
	def __init__(self, objectUID:int, quantity:int):
		self.objectUID=objectUID
		self.quantity=quantity