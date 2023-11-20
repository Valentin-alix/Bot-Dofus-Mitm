from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.collector.tax.TaxCollectorMovement import TaxCollectorMovement
class TaxCollectorMovementsOfflineMessage:
	def __init__(self, movements:list[TaxCollectorMovement]):
		self.movements=movements