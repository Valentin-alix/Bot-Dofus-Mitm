from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ServerOptionalFeaturesMessage:
	def __init__(self, features:list[int]):
		self.features=features