from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class QuestObjectiveInformations:
	def __init__(self, objectiveId:int, objectiveStatus:bool, dialogParams:list[str]):
		self.objectiveId=objectiveId
		self.objectiveStatus=objectiveStatus
		self.dialogParams=dialogParams