from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.guild.Contribution import Contribution
class GuildChestTabContributionsMessage:
	def __init__(self, contributions:list[Contribution]):
		self.contributions=contributions