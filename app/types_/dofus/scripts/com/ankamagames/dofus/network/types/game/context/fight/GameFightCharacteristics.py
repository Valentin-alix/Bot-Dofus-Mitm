from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristics import CharacterCharacteristics
class GameFightCharacteristics:
	def __init__(self, characteristics:CharacterCharacteristics, summoner:float, summoned:bool, invisibilityState:int):
		self.characteristics=characteristics
		self.summoner=summoner
		self.summoned=summoned
		self.invisibilityState=invisibilityState