from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
class FriendSpouseInformations:
	def __init__(self, spouseAccountId:int, spouseId:int, spouseName:str, spouseLevel:int, breed:int, sex:int, spouseEntityLook:EntityLook, guildInfo:GuildInformations, alignmentSide:int):
		self.spouseAccountId=spouseAccountId
		self.spouseId=spouseId
		self.spouseName=spouseName
		self.spouseLevel=spouseLevel
		self.breed=breed
		self.sex=sex
		self.spouseEntityLook=spouseEntityLook
		self.guildInfo=guildInfo
		self.alignmentSide=alignmentSide