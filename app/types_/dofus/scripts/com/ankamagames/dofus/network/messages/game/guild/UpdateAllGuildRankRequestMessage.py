from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.rank.RankInformation import RankInformation
class UpdateAllGuildRankRequestMessage:
	def __init__(self, ranks:list[RankInformation]):
		self.ranks=ranks