from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuildApplicationPresenceMessage:
	def __init__(self, isApplication:bool):
		self.isApplication=isApplication