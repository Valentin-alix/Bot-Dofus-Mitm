from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuildLevelUpMessage:
	def __init__(self, newLevel:int):
		self.newLevel=newLevel