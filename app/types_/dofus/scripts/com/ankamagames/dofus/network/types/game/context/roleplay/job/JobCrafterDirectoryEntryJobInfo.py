from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class JobCrafterDirectoryEntryJobInfo:
	def __init__(self, jobId:int, jobLevel:int, free:bool, minLevel:int):
		self.jobId=jobId
		self.jobLevel=jobLevel
		self.free=free
		self.minLevel=minLevel