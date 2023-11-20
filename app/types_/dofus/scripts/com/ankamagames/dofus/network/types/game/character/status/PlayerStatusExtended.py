from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
if TYPE_CHECKING:
	...
class PlayerStatusExtended(PlayerStatus):
	def __init__(self, message:str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.message=message