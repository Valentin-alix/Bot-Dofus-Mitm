from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MountRenamedMessage:
	def __init__(self, mountId:int, name:str):
		self.mountId=mountId
		self.name=name