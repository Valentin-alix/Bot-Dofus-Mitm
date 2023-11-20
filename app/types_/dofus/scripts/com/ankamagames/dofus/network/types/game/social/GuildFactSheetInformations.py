from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.guild.recruitment.GuildRecruitmentInformation import GuildRecruitmentInformation
class GuildFactSheetInformations(GuildInformations):
	def __init__(self, leaderId:int, nbMembers:int, lastActivityDay:int, recruitment:GuildRecruitmentInformation, nbPendingApply:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.leaderId=leaderId
		self.nbMembers=nbMembers
		self.lastActivityDay=lastActivityDay
		self.recruitment=recruitment
		self.nbPendingApply=nbPendingApply