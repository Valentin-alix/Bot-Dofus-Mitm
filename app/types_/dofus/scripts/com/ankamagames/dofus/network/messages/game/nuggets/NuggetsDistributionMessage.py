from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.nuggets.NuggetsBeneficiary import NuggetsBeneficiary
class NuggetsDistributionMessage:
	def __init__(self, beneficiaries:list[NuggetsBeneficiary]):
		self.beneficiaries=beneficiaries