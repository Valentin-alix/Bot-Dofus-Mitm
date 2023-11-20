from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class JobCrafterDirectoryListRequestMessage:
	def __init__(self, jobId:int):
		self.jobId=jobId