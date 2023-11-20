from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation
class PartyMemberInformations(CharacterBaseInformations):
	def __init__(self, lifePoints:int, maxLifePoints:int, prospecting:int, regenRate:int, initiative:int, alignmentSide:int, worldX:int, worldY:int, mapId:float, subAreaId:int, status:PlayerStatus, entities:list[PartyEntityBaseInformation], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.lifePoints=lifePoints
		self.maxLifePoints=maxLifePoints
		self.prospecting=prospecting
		self.regenRate=regenRate
		self.initiative=initiative
		self.alignmentSide=alignmentSide
		self.worldX=worldX
		self.worldY=worldY
		self.mapId=mapId
		self.subAreaId=subAreaId
		self.status=status
		self.entities=entities