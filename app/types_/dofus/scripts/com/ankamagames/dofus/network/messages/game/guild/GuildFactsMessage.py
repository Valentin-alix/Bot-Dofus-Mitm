from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.GuildFactSheetInformations import GuildFactSheetInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterMinimalSocialPublicInformations import CharacterMinimalSocialPublicInformations
class GuildFactsMessage:
	def __init__(self, infos:GuildFactSheetInformations, creationDate:int, members:list[CharacterMinimalSocialPublicInformations]):
		self.infos=infos
		self.creationDate=creationDate
		self.members=members