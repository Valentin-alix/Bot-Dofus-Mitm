from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.PaginationAnswerAbstractMessage import PaginationAnswerAbstractMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformation import AllianceFactSheetInformation
class AllianceSummaryMessage(PaginationAnswerAbstractMessage):
	def __init__(self, alliances:list[AllianceFactSheetInformation], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.alliances=alliances