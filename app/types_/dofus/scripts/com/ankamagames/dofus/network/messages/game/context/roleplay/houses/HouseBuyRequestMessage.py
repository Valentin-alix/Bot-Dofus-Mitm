from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HouseBuyRequestMessage:
	def __init__(self, proposedPrice:int):
		self.proposedPrice=proposedPrice