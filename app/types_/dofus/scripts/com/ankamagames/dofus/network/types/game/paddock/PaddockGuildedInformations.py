from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.paddock.PaddockBuyableInformations import PaddockBuyableInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
class PaddockGuildedInformations(PaddockBuyableInformations):
	def __init__(self, deserted:bool, guildInfo:GuildInformations, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.deserted=deserted
		self.guildInfo=guildInfo