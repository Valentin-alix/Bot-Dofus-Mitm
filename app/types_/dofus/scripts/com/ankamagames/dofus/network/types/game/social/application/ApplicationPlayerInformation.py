from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
class ApplicationPlayerInformation:
	def __init__(self, playerId:int, playerName:str, breed:int, sex:bool, level:int, accountId:int, accountTag:str, accountNickname:str, status:PlayerStatus):
		self.playerId=playerId
		self.playerName=playerName
		self.breed=breed
		self.sex=sex
		self.level=level
		self.accountId=accountId
		self.accountTag=accountTag
		self.accountNickname=accountNickname
		self.status=status