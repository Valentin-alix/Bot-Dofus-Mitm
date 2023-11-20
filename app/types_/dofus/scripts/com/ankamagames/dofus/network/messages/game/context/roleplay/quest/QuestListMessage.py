from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations
class QuestListMessage:
	def __init__(self, finishedQuestsIds:list[int], finishedQuestsCounts:list[int], activeQuests:list[QuestActiveInformations], reinitDoneQuestsIds:list[int]):
		self.finishedQuestsIds=finishedQuestsIds
		self.finishedQuestsCounts=finishedQuestsCounts
		self.activeQuests=activeQuests
		self.reinitDoneQuestsIds=reinitDoneQuestsIds