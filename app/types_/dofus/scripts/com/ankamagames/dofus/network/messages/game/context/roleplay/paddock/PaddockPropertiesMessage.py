from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.paddock.PaddockInstancesInformations import PaddockInstancesInformations
class PaddockPropertiesMessage:
	def __init__(self, properties:PaddockInstancesInformations):
		self.properties=properties