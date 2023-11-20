from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.paddock.PaddockInformations import PaddockInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.paddock.PaddockBuyableInformations import PaddockBuyableInformations
class PaddockInstancesInformations(PaddockInformations):
	def __init__(self, paddocks:list[PaddockBuyableInformations], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.paddocks=paddocks