from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ObjectsDeletedMessage:
	def __init__(self, objectUID:list[int]):
		self.objectUID=objectUID