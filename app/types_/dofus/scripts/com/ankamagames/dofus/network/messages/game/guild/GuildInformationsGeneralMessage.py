from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuildInformationsGeneralMessage:
	def __init__(self, abandonnedPaddock:bool, level:int, expLevelFloor:int, experience:int, expNextLevelFloor:int, creationDate:int):
		self.abandonnedPaddock=abandonnedPaddock
		self.level=level
		self.expLevelFloor=expLevelFloor
		self.experience=experience
		self.expNextLevelFloor=expNextLevelFloor
		self.creationDate=creationDate