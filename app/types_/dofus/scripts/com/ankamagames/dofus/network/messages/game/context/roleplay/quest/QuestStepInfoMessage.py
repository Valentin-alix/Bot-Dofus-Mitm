from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations
class QuestStepInfoMessage:
	def __init__(self, infos:QuestActiveInformations):
		self.infos=infos