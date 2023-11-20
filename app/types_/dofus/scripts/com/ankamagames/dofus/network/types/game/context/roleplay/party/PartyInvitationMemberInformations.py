from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation
class PartyInvitationMemberInformations(CharacterBaseInformations):
	def __init__(self, worldX:int, worldY:int, mapId:float, subAreaId:int, entities:list[PartyEntityBaseInformation], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.worldX=worldX
		self.worldY=worldY
		self.mapId=mapId
		self.subAreaId=subAreaId
		self.entities=entities