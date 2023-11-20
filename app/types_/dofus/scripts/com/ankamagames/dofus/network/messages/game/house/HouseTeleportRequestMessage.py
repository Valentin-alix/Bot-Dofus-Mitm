from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HouseTeleportRequestMessage:
	def __init__(self, houseId:int, houseInstanceId:int):
		self.houseId=houseId
		self.houseInstanceId=houseInstanceId