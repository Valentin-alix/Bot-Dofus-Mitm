from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MountHarnessColorsUpdateRequestMessage:
	def __init__(self, useHarnessColors:bool):
		self.useHarnessColors=useHarnessColors