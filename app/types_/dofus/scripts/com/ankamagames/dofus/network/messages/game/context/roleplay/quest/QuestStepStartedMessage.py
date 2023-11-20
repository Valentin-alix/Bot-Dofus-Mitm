from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class QuestStepStartedMessage:
	def __init__(self, questId:int, stepId:int):
		self.questId=questId
		self.stepId=stepId