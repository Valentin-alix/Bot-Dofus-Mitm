from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class JobBookSubscription:
	def __init__(self, jobId:int, subscribed:bool):
		self.jobId=jobId
		self.subscribed=subscribed