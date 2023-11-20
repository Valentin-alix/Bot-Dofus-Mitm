from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class JobCrafterDirectorySettings:
	def __init__(self, jobId:int, minLevel:int, free:bool):
		self.jobId=jobId
		self.minLevel=minLevel
		self.free=free