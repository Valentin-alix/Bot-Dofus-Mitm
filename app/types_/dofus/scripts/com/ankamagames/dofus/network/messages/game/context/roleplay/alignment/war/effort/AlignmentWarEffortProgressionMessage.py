from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.alignment.war.effort.AlignmentWarEffortInformation import AlignmentWarEffortInformation
class AlignmentWarEffortProgressionMessage:
	def __init__(self, effortProgressions:list[AlignmentWarEffortInformation]):
		self.effortProgressions=effortProgressions