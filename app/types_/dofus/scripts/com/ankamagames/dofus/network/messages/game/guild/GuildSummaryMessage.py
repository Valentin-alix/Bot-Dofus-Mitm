from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.PaginationAnswerAbstractMessage import PaginationAnswerAbstractMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.GuildFactSheetInformations import GuildFactSheetInformations
class GuildSummaryMessage(PaginationAnswerAbstractMessage):
	def __init__(self, guilds:list[GuildFactSheetInformations], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.guilds=guilds