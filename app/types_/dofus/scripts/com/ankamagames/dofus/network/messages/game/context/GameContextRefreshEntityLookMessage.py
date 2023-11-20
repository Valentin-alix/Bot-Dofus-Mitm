from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
class GameContextRefreshEntityLookMessage:
	def __init__(self, id:float, look:EntityLook):
		self.id=id
		self.look=look