from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.look.IndexedEntityLook import IndexedEntityLook
class HumanOptionFollowers(HumanOption):
	def __init__(self, followingCharactersLook:list[IndexedEntityLook], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.followingCharactersLook=followingCharactersLook