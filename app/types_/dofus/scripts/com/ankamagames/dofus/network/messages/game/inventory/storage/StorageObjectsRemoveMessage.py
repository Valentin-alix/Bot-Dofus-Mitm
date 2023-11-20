from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class StorageObjectsRemoveMessage:
	def __init__(self, objectUIDList:list[int]):
		self.objectUIDList=objectUIDList