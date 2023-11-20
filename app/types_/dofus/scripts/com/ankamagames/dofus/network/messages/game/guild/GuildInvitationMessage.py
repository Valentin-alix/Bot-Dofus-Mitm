from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuildInvitationMessage:
	def __init__(self, targetId:int):
		self.targetId=targetId