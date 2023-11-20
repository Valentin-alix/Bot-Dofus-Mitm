from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.actions.fight.GameActionMarkedCell import GameActionMarkedCell
class GameActionMark:
	def __init__(self, markAuthorId:float, markTeamId:int, markSpellId:int, markSpellLevel:int, markId:int, markType:int, markimpactCell:int, cells:list[GameActionMarkedCell], active:bool):
		self.markAuthorId=markAuthorId
		self.markTeamId=markTeamId
		self.markSpellId=markSpellId
		self.markSpellLevel=markSpellLevel
		self.markId=markId
		self.markType=markType
		self.markimpactCell=markimpactCell
		self.cells=cells
		self.active=active