from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class WrapperObjectDissociateRequestMessage:
	def __init__(self, hostUID:int, hostPos:int):
		self.hostUID=hostUID
		self.hostPos=hostPos