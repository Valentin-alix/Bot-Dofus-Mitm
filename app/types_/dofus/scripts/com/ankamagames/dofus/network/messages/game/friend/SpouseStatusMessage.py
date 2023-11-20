from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class SpouseStatusMessage:
	def __init__(self, hasSpouse:bool):
		self.hasSpouse=hasSpouse