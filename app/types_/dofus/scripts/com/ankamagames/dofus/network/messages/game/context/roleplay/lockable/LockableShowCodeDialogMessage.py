from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class LockableShowCodeDialogMessage:
	def __init__(self, changeOrUse:bool, codeSize:int):
		self.changeOrUse=changeOrUse
		self.codeSize=codeSize