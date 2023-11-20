from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ItemForPreset:
	def __init__(self, position:int, objGid:int, objUid:int):
		self.position=position
		self.objGid=objGid
		self.objUid=objUid