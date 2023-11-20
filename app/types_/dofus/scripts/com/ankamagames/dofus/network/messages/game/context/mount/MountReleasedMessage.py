from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MountReleasedMessage:
	def __init__(self, mountId:int):
		self.mountId=mountId