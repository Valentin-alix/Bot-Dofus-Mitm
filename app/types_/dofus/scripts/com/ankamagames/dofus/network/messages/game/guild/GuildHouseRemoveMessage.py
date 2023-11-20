from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuildHouseRemoveMessage:
	def __init__(self, houseId:int, instanceId:int, secondHand:bool):
		self.houseId=houseId
		self.instanceId=instanceId
		self.secondHand=secondHand