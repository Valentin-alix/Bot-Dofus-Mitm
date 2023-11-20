from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
class MapComplementaryInformationsDataInHavenBagMessage(MapComplementaryInformationsDataMessage):
	def __init__(self, ownerInformations:CharacterMinimalInformations, theme:int, roomId:int, maxRoomId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ownerInformations=ownerInformations
		self.theme=theme
		self.roomId=roomId
		self.maxRoomId=maxRoomId