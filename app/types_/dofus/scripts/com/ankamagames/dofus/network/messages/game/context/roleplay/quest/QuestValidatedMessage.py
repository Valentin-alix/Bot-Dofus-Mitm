from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class QuestValidatedMessage:
	def __init__(self, questId:int):
		self.questId=questId