from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.approach.ServerSessionConstant import ServerSessionConstant
if TYPE_CHECKING:
	...
class ServerSessionConstantLong(ServerSessionConstant):
	def __init__(self, value:float, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.value=value