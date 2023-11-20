from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformation import AllianceInformation
class AllianceApplicationIsAnsweredMessage:
	def __init__(self, accepted:bool, allianceInformation:AllianceInformation):
		self.accepted=accepted
		self.allianceInformation=allianceInformation