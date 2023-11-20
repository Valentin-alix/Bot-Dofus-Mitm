from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class SlaveNoLongerControledMessage:
	def __init__(self, masterId:float, slaveId:float):
		self.masterId=masterId
		self.slaveId=slaveId