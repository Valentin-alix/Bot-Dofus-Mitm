from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaRankInfos import ArenaRankInfos
class GameRolePlayArenaUpdatePlayerInfosMessage:
	def __init__(self, solo:ArenaRankInfos):
		self.solo=solo