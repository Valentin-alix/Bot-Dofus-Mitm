from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.GuildFactSheetInformations import GuildFactSheetInformations
if TYPE_CHECKING:
	...
class GuildInsiderFactSheetInformations(GuildFactSheetInformations):
	def __init__(self, leaderName:str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.leaderName=leaderName