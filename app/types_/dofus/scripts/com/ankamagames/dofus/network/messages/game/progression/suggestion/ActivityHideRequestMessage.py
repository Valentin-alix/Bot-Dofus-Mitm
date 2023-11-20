from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ActivityHideRequestMessage:
	def __init__(self, activityId:int):
		self.activityId=activityId