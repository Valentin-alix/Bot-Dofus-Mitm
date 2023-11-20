from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TeleportBuddiesRequestedMessage:
	def __init__(self, dungeonId:int, inviterId:int, invalidBuddiesIds:list[int]):
		self.dungeonId=dungeonId
		self.inviterId=inviterId
		self.invalidBuddiesIds=invalidBuddiesIds