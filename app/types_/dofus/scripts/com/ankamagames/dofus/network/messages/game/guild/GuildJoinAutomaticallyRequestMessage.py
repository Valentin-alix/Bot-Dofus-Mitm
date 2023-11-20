from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuildJoinAutomaticallyRequestMessage:
	def __init__(self, guildId:int):
		self.guildId=guildId