from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class BasicDateMessage:
	def __init__(self, day:int, month:int, year:int):
		self.day=day
		self.month=month
		self.year=year