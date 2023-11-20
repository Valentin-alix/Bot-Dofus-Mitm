from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.MapRunningFightDetailsMessage import MapRunningFightDetailsMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeam import NamedPartyTeam
class MapRunningFightDetailsExtendedMessage(MapRunningFightDetailsMessage):
	def __init__(self, namedPartyTeams:list[NamedPartyTeam], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.namedPartyTeams=namedPartyTeams