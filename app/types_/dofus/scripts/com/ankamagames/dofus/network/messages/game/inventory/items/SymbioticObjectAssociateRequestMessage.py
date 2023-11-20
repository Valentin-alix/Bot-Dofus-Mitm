from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class SymbioticObjectAssociateRequestMessage:
	def __init__(self, symbioteUID:int, symbiotePos:int, hostUID:int, hostPos:int):
		self.symbioteUID=symbioteUID
		self.symbiotePos=symbiotePos
		self.hostUID=hostUID
		self.hostPos=hostPos