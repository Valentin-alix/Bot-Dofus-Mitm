from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.web.haapi.BufferInformation import BufferInformation
class HaapiBufferListMessage:
	def __init__(self, buffers:list[BufferInformation]):
		self.buffers=buffers