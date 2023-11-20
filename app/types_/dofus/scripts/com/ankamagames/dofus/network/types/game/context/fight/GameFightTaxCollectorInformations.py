from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightAIInformations import GameFightAIInformations
if TYPE_CHECKING:
	...
class GameFightTaxCollectorInformations(GameFightAIInformations):
	def __init__(self, firstNameId:int, lastNameId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.firstNameId=firstNameId
		self.lastNameId=lastNameId