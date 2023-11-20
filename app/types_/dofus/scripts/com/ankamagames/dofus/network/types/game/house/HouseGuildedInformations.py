from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
class HouseGuildedInformations(HouseInstanceInformations):
	def __init__(self, guildInfo:GuildInformations, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.guildInfo=guildInfo