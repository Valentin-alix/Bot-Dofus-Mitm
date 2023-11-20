from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation
if TYPE_CHECKING:
	...
class PartyEntityMemberInformation(PartyEntityBaseInformation):
	def __init__(self, initiative:int, lifePoints:int, maxLifePoints:int, prospecting:int, regenRate:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.initiative=initiative
		self.lifePoints=lifePoints
		self.maxLifePoints=maxLifePoints
		self.prospecting=prospecting
		self.regenRate=regenRate