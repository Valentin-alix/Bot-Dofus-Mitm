from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.house.AccountHouseInformations import AccountHouseInformations
class AccountHouseMessage:
	def __init__(self, houses:list[AccountHouseInformations]):
		self.houses=houses