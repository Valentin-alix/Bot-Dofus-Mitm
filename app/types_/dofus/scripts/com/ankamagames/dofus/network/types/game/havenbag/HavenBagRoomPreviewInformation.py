from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HavenBagRoomPreviewInformation:
	def __init__(self, roomId:int, themeId:int):
		self.roomId=roomId
		self.themeId=themeId