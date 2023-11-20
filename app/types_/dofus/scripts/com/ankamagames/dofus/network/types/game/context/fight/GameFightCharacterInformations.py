from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterNamedInformations import GameFightFighterNamedInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations
class GameFightCharacterInformations(GameFightFighterNamedInformations):
	def __init__(self, level:int, alignmentInfos:ActorAlignmentInformations, breed:int, sex:bool, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.level=level
		self.alignmentInfos=alignmentInfos
		self.breed=breed
		self.sex=sex