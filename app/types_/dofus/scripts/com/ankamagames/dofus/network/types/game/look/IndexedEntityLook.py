from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
class IndexedEntityLook:
	def __init__(self, look:EntityLook, index:int):
		self.look=look
		self.index=index