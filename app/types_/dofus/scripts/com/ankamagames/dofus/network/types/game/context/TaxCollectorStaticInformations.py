from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformation import AllianceInformation
class TaxCollectorStaticInformations:
	def __init__(self, firstNameId:int, lastNameId:int, allianceIdentity:AllianceInformation, callerId:int):
		self.firstNameId=firstNameId
		self.lastNameId=lastNameId
		self.allianceIdentity=allianceIdentity
		self.callerId=callerId