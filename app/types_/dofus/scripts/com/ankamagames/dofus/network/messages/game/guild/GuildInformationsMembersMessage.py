from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.guild.GuildMemberInfo import GuildMemberInfo
class GuildInformationsMembersMessage:
	def __init__(self, members:list[GuildMemberInfo]):
		self.members=members