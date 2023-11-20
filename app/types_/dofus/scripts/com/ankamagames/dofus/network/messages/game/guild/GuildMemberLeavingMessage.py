from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuildMemberLeavingMessage:
	def __init__(self, kicked:bool, memberId:int):
		self.kicked=kicked
		self.memberId=memberId