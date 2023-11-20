from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TeleportToBuddyCloseMessage:
	def __init__(self, dungeonId:int, buddyId:int):
		self.dungeonId=dungeonId
		self.buddyId=buddyId