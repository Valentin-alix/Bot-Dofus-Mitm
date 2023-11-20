from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class JobExperience:
	def __init__(self, jobId:int, jobLevel:int, jobXP:int, jobXpLevelFloor:int, jobXpNextLevelFloor:int):
		self.jobId=jobId
		self.jobLevel=jobLevel
		self.jobXP=jobXP
		self.jobXpLevelFloor=jobXpLevelFloor
		self.jobXpNextLevelFloor=jobXpNextLevelFloor