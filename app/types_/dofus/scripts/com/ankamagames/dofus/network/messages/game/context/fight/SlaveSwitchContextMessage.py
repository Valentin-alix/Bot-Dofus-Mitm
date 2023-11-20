from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.SpellItem import SpellItem
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut
class SlaveSwitchContextMessage:
	def __init__(self, masterId:float, slaveId:float, slaveTurn:int, slaveSpells:list[SpellItem], slaveStats:CharacterCharacteristicsInformations, shortcuts:list[Shortcut]):
		self.masterId=masterId
		self.slaveId=slaveId
		self.slaveTurn=slaveTurn
		self.slaveSpells=slaveSpells
		self.slaveStats=slaveStats
		self.shortcuts=shortcuts