from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformation import AllianceInformation
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.alliance.KohAllianceRoleMembers import KohAllianceRoleMembers
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.alliance.KohScore import KohScore
class KohAllianceInfo:
	def __init__(self, alliance:AllianceInformation, memberCount:int, kohAllianceRoleMembers:list[KohAllianceRoleMembers], scores:list[KohScore], matchDominationScores:int):
		self.alliance=alliance
		self.memberCount=memberCount
		self.kohAllianceRoleMembers=kohAllianceRoleMembers
		self.scores=scores
		self.matchDominationScores=matchDominationScores