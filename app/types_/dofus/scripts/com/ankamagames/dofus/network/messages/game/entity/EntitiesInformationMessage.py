from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.entity.EntityInformation import EntityInformation
class EntitiesInformationMessage:
	def __init__(self, entities:list[EntityInformation]):
		self.entities=entities