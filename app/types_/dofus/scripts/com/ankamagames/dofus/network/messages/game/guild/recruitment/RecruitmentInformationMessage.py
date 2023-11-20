from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.guild.recruitment.GuildRecruitmentInformation import GuildRecruitmentInformation
class RecruitmentInformationMessage:
	def __init__(self, recruitmentData:GuildRecruitmentInformation):
		self.recruitmentData=recruitmentData