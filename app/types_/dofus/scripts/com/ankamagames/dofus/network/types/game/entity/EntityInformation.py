from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class EntityInformation:
	def __init__(self, id:int, experience:int, status:bool):
		self.id=id
		self.experience=experience
		self.status=status