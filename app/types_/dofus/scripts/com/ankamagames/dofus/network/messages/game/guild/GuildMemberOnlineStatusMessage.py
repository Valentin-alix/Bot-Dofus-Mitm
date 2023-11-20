from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuildMemberOnlineStatusMessage:
	def __init__(self, memberId:int, online:bool):
		self.memberId=memberId
		self.online=online