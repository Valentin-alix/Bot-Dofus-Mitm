from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class InteractiveUseErrorMessage:
	def __init__(self, elemId:int, skillInstanceUid:int):
		self.elemId=elemId
		self.skillInstanceUid=skillInstanceUid