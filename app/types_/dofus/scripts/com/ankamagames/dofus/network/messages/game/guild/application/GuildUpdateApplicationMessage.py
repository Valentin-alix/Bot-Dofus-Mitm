from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuildUpdateApplicationMessage:
	def __init__(self, applyText:str, guildId:int):
		self.applyText=applyText
		self.guildId=guildId