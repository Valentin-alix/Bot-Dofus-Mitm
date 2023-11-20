from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class NotificationListMessage:
	def __init__(self, flags:list[int]):
		self.flags=flags