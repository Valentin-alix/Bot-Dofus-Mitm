from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
class HumanOptionGuild(HumanOption):
	def __init__(self, guildInformations:GuildInformations, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.guildInformations=guildInformations