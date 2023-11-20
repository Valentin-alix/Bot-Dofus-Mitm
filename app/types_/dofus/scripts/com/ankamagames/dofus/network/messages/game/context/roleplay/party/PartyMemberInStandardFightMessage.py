from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMemberInFightMessage import AbstractPartyMemberInFightMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.MapCoordinatesExtended import MapCoordinatesExtended
class PartyMemberInStandardFightMessage(AbstractPartyMemberInFightMessage):
	def __init__(self, fightMap:MapCoordinatesExtended, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fightMap=fightMap