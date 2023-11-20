from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.guild.application.GuildPlayerApplicationAbstractMessage import GuildPlayerApplicationAbstractMessage
if TYPE_CHECKING:
	...
class GuildPlayerNoApplicationInformationMessage(GuildPlayerApplicationAbstractMessage):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		...