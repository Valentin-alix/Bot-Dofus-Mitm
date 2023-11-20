from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ServerSettingsMessage:
	def __init__(self, lang:str, community:int, gameType:int, arenaLeaveBanTime:int, itemMaxLevel:int):
		self.lang=lang
		self.community=community
		self.gameType=gameType
		self.arenaLeaveBanTime=arenaLeaveBanTime
		self.itemMaxLevel=itemMaxLevel