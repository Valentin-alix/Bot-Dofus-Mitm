from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations
class TaxCollectorDialogQuestionBasicMessage:
	def __init__(self, allianceInfo:BasicAllianceInformations):
		self.allianceInfo=allianceInfo