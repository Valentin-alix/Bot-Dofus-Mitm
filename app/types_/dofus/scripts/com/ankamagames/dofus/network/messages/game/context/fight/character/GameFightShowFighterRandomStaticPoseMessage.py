from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.fight.character.GameFightShowFighterMessage import GameFightShowFighterMessage
if TYPE_CHECKING:
	...
class GameFightShowFighterRandomStaticPoseMessage(GameFightShowFighterMessage):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		...