from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class FriendStatusShareStateMessage:
	def __init__(self, share:bool):
		self.share=share