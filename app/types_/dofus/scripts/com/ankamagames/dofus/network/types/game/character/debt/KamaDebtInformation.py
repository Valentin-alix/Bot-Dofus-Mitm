from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.debt.DebtInformation import DebtInformation
if TYPE_CHECKING:
	...
class KamaDebtInformation(DebtInformation):
	def __init__(self, kamas:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.kamas=kamas