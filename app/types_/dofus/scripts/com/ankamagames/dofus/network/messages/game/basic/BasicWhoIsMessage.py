from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.AbstractSocialGroupInfos import AbstractSocialGroupInfos
class BasicWhoIsMessage:
	def __init__(self, position:int, accountTag:AccountTagInformation, accountId:int, playerName:str, playerId:int, areaId:int, serverId:int, originServerId:int, socialGroups:list[AbstractSocialGroupInfos], playerState:int):
		self.position=position
		self.accountTag=accountTag
		self.accountId=accountId
		self.playerName=playerName
		self.playerId=playerId
		self.areaId=areaId
		self.serverId=serverId
		self.originServerId=originServerId
		self.socialGroups=socialGroups
		self.playerState=playerState