from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
if TYPE_CHECKING:
	...
class HumanOptionOrnament(HumanOption):
	def __init__(self, ornamentId:int, level:int, leagueId:int, ladderPosition:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ornamentId=ornamentId
		self.level=level
		self.leagueId=leagueId
		self.ladderPosition=ladderPosition