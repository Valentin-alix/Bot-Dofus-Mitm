from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformation import AllianceInformation
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.alliance.recruitment.AllianceRecruitmentInformation import AllianceRecruitmentInformation
class AllianceFactSheetInformation(AllianceInformation):
	def __init__(self, creationDate:int, nbMembers:int, nbSubarea:int, nbTaxCollectors:int, recruitment:AllianceRecruitmentInformation, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.creationDate=creationDate
		self.nbMembers=nbMembers
		self.nbSubarea=nbSubarea
		self.nbTaxCollectors=nbTaxCollectors
		self.recruitment=recruitment