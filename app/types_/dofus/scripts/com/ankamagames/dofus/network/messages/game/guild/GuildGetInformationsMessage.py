from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuildGetInformationsMessage:
	def __init__(self, infoType:int):
		self.infoType=infoType