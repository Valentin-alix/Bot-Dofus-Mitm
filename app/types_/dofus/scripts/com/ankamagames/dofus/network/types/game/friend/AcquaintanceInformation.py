from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.friend.AbstractContactInformations import AbstractContactInformations
if TYPE_CHECKING:
	...
class AcquaintanceInformation(AbstractContactInformations):
	def __init__(self, playerState:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.playerState=playerState