from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class UnfollowQuestObjectiveRequestMessage:
	def __init__(self, questId:int, objectiveId:int):
		self.questId=questId
		self.objectiveId=objectiveId