from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.houses.HouseSellRequestMessage import HouseSellRequestMessage
if TYPE_CHECKING:
	...
class HouseSellFromInsideRequestMessage(HouseSellRequestMessage):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		...