from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class JobCrafterDirectoryRemoveMessage:
	def __init__(self, jobId:int, playerId:int):
		self.jobId=jobId
		self.playerId=playerId