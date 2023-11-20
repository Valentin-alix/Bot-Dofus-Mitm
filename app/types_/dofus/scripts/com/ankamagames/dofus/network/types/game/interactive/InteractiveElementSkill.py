from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class InteractiveElementSkill:
	def __init__(self, skillId:int, skillInstanceUid:int):
		self.skillId=skillId
		self.skillInstanceUid=skillInstanceUid