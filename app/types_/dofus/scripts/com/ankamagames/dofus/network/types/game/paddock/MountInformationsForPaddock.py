from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MountInformationsForPaddock:
	def __init__(self, modelId:int, name:str, ownerName:str):
		self.modelId=modelId
		self.name=name
		self.ownerName=ownerName