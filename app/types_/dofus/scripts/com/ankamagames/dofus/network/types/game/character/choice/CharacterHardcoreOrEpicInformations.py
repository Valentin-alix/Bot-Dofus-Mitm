from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
if TYPE_CHECKING:
	...
class CharacterHardcoreOrEpicInformations(CharacterBaseInformations):
	def __init__(self, deathState:int, deathCount:int, deathMaxLevel:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.deathState=deathState
		self.deathCount=deathCount
		self.deathMaxLevel=deathMaxLevel