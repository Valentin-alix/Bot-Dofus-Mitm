from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
class GuildListMessage:
	def __init__(self, guilds:list[GuildInformations]):
		self.guilds=guilds