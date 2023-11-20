from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.guild.GuildMemberInfo import GuildMemberInfo
class GuildInformationsMemberUpdateMessage:
	def __init__(self, member:GuildMemberInfo):
		self.member=member