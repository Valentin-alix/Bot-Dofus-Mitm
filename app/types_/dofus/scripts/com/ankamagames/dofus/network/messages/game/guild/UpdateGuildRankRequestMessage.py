from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.rank.RankInformation import RankInformation
class UpdateGuildRankRequestMessage:
	def __init__(self, rank:RankInformation):
		self.rank=rank