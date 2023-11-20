from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.GameContextActorPositionInformations import GameContextActorPositionInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
class GameContextActorInformations(GameContextActorPositionInformations):
	def __init__(self, look:EntityLook, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.look=look