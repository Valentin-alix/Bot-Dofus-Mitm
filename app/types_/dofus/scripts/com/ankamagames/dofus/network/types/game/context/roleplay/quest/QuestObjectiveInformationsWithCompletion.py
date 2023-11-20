from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestObjectiveInformations import QuestObjectiveInformations
if TYPE_CHECKING:
	...
class QuestObjectiveInformationsWithCompletion(QuestObjectiveInformations):
	def __init__(self, curCompletion:int, maxCompletion:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.curCompletion=curCompletion
		self.maxCompletion=maxCompletion