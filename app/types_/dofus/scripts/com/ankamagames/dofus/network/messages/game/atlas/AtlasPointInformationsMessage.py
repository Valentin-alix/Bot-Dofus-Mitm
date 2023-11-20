from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.AtlasPointsInformations import AtlasPointsInformations
class AtlasPointInformationsMessage:
	def __init__(self, type:AtlasPointsInformations):
		self.type=type