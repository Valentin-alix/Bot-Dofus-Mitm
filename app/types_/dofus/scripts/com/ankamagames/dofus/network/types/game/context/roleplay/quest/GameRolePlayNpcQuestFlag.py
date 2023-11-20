from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayNpcQuestFlag:
	def __init__(self, questsToValidId:list[int], questsToStartId:list[int]):
		self.questsToValidId=questsToValidId
		self.questsToStartId=questsToStartId