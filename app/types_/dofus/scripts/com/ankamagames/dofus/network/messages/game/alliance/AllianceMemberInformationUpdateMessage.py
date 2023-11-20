from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.alliance.AllianceMemberInfo import AllianceMemberInfo
class AllianceMemberInformationUpdateMessage:
	def __init__(self, member:AllianceMemberInfo):
		self.member=member