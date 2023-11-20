from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.ShowCellMessage import ShowCellMessage
if TYPE_CHECKING:
	...
class ShowCellSpectatorMessage(ShowCellMessage):
	def __init__(self, playerName:str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.playerName=playerName