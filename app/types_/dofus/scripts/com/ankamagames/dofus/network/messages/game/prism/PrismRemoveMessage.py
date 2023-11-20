from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.prism.PrismGeolocalizedInformation import PrismGeolocalizedInformation
class PrismRemoveMessage:
	def __init__(self, prism:PrismGeolocalizedInformation):
		self.prism=prism