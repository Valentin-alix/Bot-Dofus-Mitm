from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class NotificationByServerMessage:
	def __init__(self, id:int, parameters:list[str], forceOpen:bool):
		self.id=id
		self.parameters=parameters
		self.forceOpen=forceOpen