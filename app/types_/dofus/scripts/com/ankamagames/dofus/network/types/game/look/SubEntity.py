from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
class SubEntity:
	def __init__(self, bindingPointCategory:int, bindingPointIndex:int, subEntityLook:EntityLook):
		self.bindingPointCategory=bindingPointCategory
		self.bindingPointIndex=bindingPointIndex
		self.subEntityLook=subEntityLook