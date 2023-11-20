from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.alliance.recruitment.AllianceRecruitmentInformation import AllianceRecruitmentInformation
class AllianceUpdateRecruitmentInformationMessage:
	def __init__(self, recruitmentData:AllianceRecruitmentInformation):
		self.recruitmentData=recruitmentData