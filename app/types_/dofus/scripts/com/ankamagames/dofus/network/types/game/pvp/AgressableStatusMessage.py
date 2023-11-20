from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AgressableStatusMessage:
	def __init__(self, playerId:int, enable:int, roleAvAId:int, pictoScore:int):
		self.playerId=playerId
		self.enable=enable
		self.roleAvAId=roleAvAId
		self.pictoScore=pictoScore