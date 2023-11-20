from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class CharacterCanBeCreatedResultMessage:
	def __init__(self, yesYouCan:bool):
		self.yesYouCan=yesYouCan