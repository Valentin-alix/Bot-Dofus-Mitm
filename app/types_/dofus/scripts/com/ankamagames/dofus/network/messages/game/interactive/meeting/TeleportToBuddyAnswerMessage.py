from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TeleportToBuddyAnswerMessage:
	def __init__(self, dungeonId:int, buddyId:int, accept:bool):
		self.dungeonId=dungeonId
		self.buddyId=buddyId
		self.accept=accept