from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ObjectItemInRolePlay:
	def __init__(self, cellId:int, objectGID:int):
		self.cellId=cellId
		self.objectGID=objectGID