from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ActivityLockRequestMessage:
	def __init__(self, activityId:int, lock:bool):
		self.activityId=activityId
		self.lock=lock