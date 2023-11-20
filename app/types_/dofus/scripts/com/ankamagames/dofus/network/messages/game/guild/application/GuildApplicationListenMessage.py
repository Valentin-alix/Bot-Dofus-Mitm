from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuildApplicationListenMessage:
	def __init__(self, listen:bool):
		self.listen=listen