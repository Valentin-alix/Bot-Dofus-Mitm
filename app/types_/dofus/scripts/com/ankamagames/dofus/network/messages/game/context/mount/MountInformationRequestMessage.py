from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MountInformationRequestMessage:
	def __init__(self, id:float, time:float):
		self.id=id
		self.time=time