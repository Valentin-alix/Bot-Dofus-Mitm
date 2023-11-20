from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MonsterInGroupLightInformations:
	def __init__(self, genericId:int, grade:int, level:int):
		self.genericId=genericId
		self.grade=grade
		self.level=level