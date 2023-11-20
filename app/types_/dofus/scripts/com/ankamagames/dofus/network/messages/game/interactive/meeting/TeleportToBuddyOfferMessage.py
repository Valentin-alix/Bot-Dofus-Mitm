from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TeleportToBuddyOfferMessage:
	def __init__(self, dungeonId:int, buddyId:int, timeLeft:int):
		self.dungeonId=dungeonId
		self.buddyId=buddyId
		self.timeLeft=timeLeft