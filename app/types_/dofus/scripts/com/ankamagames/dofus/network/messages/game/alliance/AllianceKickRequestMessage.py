from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AllianceKickRequestMessage:
	def __init__(self, kickedId:int):
		self.kickedId=kickedId