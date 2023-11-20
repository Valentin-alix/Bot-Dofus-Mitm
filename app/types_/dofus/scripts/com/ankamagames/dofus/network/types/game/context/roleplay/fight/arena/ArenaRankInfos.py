from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaRanking import ArenaRanking
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaLeagueRanking import ArenaLeagueRanking
class ArenaRankInfos:
	def __init__(self, victoryCount:int, fightcount:int, numFightNeededForLadder:int, ranking:ArenaRanking|None=None , leagueRanking:ArenaLeagueRanking|None=None ):
		self.ranking=ranking
		self.leagueRanking=leagueRanking
		self.victoryCount=victoryCount
		self.fightcount=fightcount
		self.numFightNeededForLadder=numFightNeededForLadder