from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.fight.GameFightJoinMessage import GameFightJoinMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeam import NamedPartyTeam
class GameFightSpectatorJoinMessage(GameFightJoinMessage):
	def __init__(self, namedPartyTeams:list[NamedPartyTeam], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.namedPartyTeams=namedPartyTeams