from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.debt.DebtInformation import DebtInformation
class DebtsUpdateMessage:
	def __init__(self, action:int, debts:list[DebtInformation]):
		self.action=action
		self.debts=debts