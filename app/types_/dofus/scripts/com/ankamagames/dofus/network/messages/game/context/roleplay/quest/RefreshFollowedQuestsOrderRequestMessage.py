from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class RefreshFollowedQuestsOrderRequestMessage:
	def __init__(self, quests:list[int]):
		self.quests=quests