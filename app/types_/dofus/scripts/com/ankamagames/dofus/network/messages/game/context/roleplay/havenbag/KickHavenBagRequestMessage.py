from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class KickHavenBagRequestMessage:
	def __init__(self, guestId:int):
		self.guestId=guestId