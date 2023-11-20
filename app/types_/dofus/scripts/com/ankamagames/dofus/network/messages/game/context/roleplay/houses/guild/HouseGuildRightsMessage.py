from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
class HouseGuildRightsMessage:
	def __init__(self, houseId:int, instanceId:int, secondHand:bool, guildInfo:GuildInformations, rights:int):
		self.houseId=houseId
		self.instanceId=instanceId
		self.secondHand=secondHand
		self.guildInfo=guildInfo
		self.rights=rights