from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.LeagueFriendInformations import LeagueFriendInformations
class GameRolePlayArenaInvitationCandidatesAnswerMessage:
	def __init__(self, candidates:list[LeagueFriendInformations]):
		self.candidates=candidates