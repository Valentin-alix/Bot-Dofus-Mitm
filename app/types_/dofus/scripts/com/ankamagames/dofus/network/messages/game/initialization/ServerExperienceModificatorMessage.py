from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ServerExperienceModificatorMessage:
	def __init__(self, experiencePercent:int):
		self.experiencePercent=experiencePercent