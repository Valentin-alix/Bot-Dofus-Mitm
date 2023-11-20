from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class UpdateSelfAgressableStatusMessage:
	def __init__(self, status:int, probationTime:float, roleAvAId:int, pictoScore:int):
		self.status=status
		self.probationTime=probationTime
		self.roleAvAId=roleAvAId
		self.pictoScore=pictoScore