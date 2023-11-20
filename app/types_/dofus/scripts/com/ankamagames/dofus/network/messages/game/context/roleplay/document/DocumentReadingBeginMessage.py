from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class DocumentReadingBeginMessage:
	def __init__(self, documentId:int):
		self.documentId=documentId