from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import GameContextActorInformations
if TYPE_CHECKING:
	...
class GameRolePlayActorInformations(GameContextActorInformations):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		...