from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MountRenameRequestMessage:
	def __init__(self, name:str, mountId:int):
		self.name=name
		self.mountId=mountId