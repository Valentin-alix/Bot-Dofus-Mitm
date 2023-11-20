from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.approach.ServerSessionConstant import ServerSessionConstant
class ServerSessionConstantsMessage:
	def __init__(self, variables:list[ServerSessionConstant]):
		self.variables=variables