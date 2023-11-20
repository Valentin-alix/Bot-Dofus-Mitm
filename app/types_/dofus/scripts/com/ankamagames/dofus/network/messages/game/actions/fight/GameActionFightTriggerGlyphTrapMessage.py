from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
if TYPE_CHECKING:
	...
class GameActionFightTriggerGlyphTrapMessage(AbstractGameActionMessage):
	def __init__(self, markId:int, markImpactCell:int, triggeringCharacterId:float, triggeredSpellId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.markId=markId
		self.markImpactCell=markImpactCell
		self.triggeringCharacterId=triggeringCharacterId
		self.triggeredSpellId=triggeredSpellId