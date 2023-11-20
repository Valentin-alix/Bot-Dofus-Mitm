from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.actions.fight.AbstractGameActionFightTargetedAbilityMessage import AbstractGameActionFightTargetedAbilityMessage
if TYPE_CHECKING:
	...
class GameActionFightCloseCombatMessage(AbstractGameActionFightTargetedAbilityMessage):
	def __init__(self, weaponGenericId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.weaponGenericId=weaponGenericId