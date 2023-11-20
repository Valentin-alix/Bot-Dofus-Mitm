from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.collector.tax.TaxCollectorInformations import TaxCollectorInformations
class ConfirmationOfListeningTaxCollectorUpdatesMessage:
	def __init__(self, information:TaxCollectorInformations):
		self.information=information