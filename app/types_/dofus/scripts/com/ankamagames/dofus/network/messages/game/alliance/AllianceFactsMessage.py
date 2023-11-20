from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformation import AllianceFactSheetInformation
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterMinimalSocialPublicInformations import CharacterMinimalSocialPublicInformations
class AllianceFactsMessage:
	def __init__(self, infos:AllianceFactSheetInformation, members:list[CharacterMinimalSocialPublicInformations], controlledSubareaIds:list[int], leaderCharacterId:int, leaderCharacterName:str):
		self.infos=infos
		self.members=members
		self.controlledSubareaIds=controlledSubareaIds
		self.leaderCharacterId=leaderCharacterId
		self.leaderCharacterName=leaderCharacterName