from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.entity.EntityInformation import EntityInformation
class EntityInformationMessage:
	def __init__(self, entity:EntityInformation):
		self.entity=entity