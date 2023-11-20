from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations
if TYPE_CHECKING:
	...
class ActorExtendedAlignmentInformations(ActorAlignmentInformations):
	def __init__(self, honor:int, honorGradeFloor:int, honorNextGradeFloor:int, aggressable:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.honor=honor
		self.honorGradeFloor=honorGradeFloor
		self.honorNextGradeFloor=honorNextGradeFloor
		self.aggressable=aggressable