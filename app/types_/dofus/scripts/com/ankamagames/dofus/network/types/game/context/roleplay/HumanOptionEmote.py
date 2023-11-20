from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
if TYPE_CHECKING:
	...
class HumanOptionEmote(HumanOption):
	def __init__(self, emoteId:int, emoteStartTime:float, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.emoteId=emoteId
		self.emoteStartTime=emoteStartTime