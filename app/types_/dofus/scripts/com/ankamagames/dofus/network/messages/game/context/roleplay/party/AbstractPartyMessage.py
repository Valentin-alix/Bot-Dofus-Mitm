from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AbstractPartyMessage:
	def __init__(self, partyId:int):
		self.partyId=partyId