from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.job.DecraftedItemStackInfo import DecraftedItemStackInfo
class DecraftResultMessage:
	def __init__(self, results:list[DecraftedItemStackInfo]):
		self.results=results