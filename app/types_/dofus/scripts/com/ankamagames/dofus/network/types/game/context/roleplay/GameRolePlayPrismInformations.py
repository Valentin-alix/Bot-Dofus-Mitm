from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation
class GameRolePlayPrismInformations(GameRolePlayActorInformations):
	def __init__(self, prism:PrismInformation, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.prism=prism