from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.TaxCollectorStaticInformations import TaxCollectorStaticInformations
class GameRolePlayTaxCollectorInformations(GameRolePlayActorInformations):
	def __init__(self, identification:TaxCollectorStaticInformations, taxCollectorAttack:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.identification=identification
		self.taxCollectorAttack=taxCollectorAttack