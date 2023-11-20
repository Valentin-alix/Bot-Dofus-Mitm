from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.collector.tax.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.fight.ProtectedEntityWaitingForHelpInfo import ProtectedEntityWaitingForHelpInfo
class TaxCollectorWaitingForHelpInformations(TaxCollectorComplementaryInformations):
	def __init__(self, waitingForHelpInfo:ProtectedEntityWaitingForHelpInfo, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.waitingForHelpInfo=waitingForHelpInfo