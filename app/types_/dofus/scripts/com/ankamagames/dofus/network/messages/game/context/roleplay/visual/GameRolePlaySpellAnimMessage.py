from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlaySpellAnimMessage:
	def __init__(self, casterId:int, targetCellId:int, spellId:int, spellLevel:int, direction:int):
		self.casterId=casterId
		self.targetCellId=targetCellId
		self.spellId=spellId
		self.spellLevel=spellLevel
		self.direction=direction