from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.friend.IgnoredInformations import IgnoredInformations
if TYPE_CHECKING:
	...
class IgnoredOnlineInformations(IgnoredInformations):
	def __init__(self, playerId:int, playerName:str, breed:int, sex:bool, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.playerId=playerId
		self.playerName=playerName
		self.breed=breed
		self.sex=sex