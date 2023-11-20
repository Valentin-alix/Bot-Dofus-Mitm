from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage
if TYPE_CHECKING:
	...
class PartyUpdateLightMessage(AbstractPartyEventMessage):
	def __init__(self, id:int, lifePoints:int, maxLifePoints:int, prospecting:int, regenRate:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.id=id
		self.lifePoints=lifePoints
		self.maxLifePoints=maxLifePoints
		self.prospecting=prospecting
		self.regenRate=regenRate