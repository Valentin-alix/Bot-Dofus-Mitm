from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations
if TYPE_CHECKING:
	...
class GameRolePlayMountInformations(GameRolePlayNamedActorInformations):
	def __init__(self, ownerName:str, level:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ownerName=ownerName
		self.level=level