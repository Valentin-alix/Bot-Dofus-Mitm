from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic
if TYPE_CHECKING:
	...
class CharacterCharacteristicDetailed(CharacterCharacteristic):
	def __init__(self, base:int, additional:int, objectsAndMountBonus:int, alignGiftBonus:int, contextModif:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.base=base
		self.additional=additional
		self.objectsAndMountBonus=objectsAndMountBonus
		self.alignGiftBonus=alignGiftBonus
		self.contextModif=contextModif