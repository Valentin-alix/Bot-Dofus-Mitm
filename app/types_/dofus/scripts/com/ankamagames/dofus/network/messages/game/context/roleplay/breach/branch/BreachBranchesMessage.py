from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.breach.ExtendedBreachBranch import ExtendedBreachBranch
class BreachBranchesMessage:
	def __init__(self, branches:list[ExtendedBreachBranch]):
		self.branches=branches