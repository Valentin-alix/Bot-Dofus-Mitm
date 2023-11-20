from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class OpenGuideBookMessage:
	def __init__(self, articleId:int):
		self.articleId=articleId