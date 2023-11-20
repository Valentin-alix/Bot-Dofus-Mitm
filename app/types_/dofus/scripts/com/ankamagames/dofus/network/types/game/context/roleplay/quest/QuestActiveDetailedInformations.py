from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestObjectiveInformations import QuestObjectiveInformations
class QuestActiveDetailedInformations(QuestActiveInformations):
	def __init__(self, stepId:int, objectives:list[QuestObjectiveInformations], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.stepId=stepId
		self.objectives=objectives