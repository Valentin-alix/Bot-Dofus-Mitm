from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class StorageObjectRemoveMessage:
	def __init__(self, objectUID:int):
		self.objectUID=objectUID