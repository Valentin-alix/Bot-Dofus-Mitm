from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.actions.fight.AbstractGameActionFightTargetedAbilityMessage import AbstractGameActionFightTargetedAbilityMessage
if TYPE_CHECKING:
	...
class GameActionFightSpellCastMessage(AbstractGameActionFightTargetedAbilityMessage):
	def __init__(self, spellId:int, spellLevel:int, portalsIds:list[int], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.spellId=spellId
		self.spellLevel=spellLevel
		self.portalsIds=portalsIds