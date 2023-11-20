from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.restriction.ActorRestrictionsInformations import ActorRestrictionsInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
class HumanInformations:
	def __init__(self, restrictions:ActorRestrictionsInformations, sex:bool, options:list[HumanOption]):
		self.restrictions=restrictions
		self.sex=sex
		self.options=options