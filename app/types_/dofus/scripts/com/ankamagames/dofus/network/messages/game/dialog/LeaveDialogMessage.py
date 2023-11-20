from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class LeaveDialogMessage:
	def __init__(self, dialogType:int):
		self.dialogType=dialogType