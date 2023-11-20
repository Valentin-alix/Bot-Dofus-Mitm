from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
class GameRolePlayShowActorMessage:
	def __init__(self, informations:GameRolePlayActorInformations):
		self.informations=informations