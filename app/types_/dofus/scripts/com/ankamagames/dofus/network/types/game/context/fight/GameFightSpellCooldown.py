from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightSpellCooldown:
	def __init__(self, spellId:int, cooldown:int):
		self.spellId=spellId
		self.cooldown=cooldown