from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class Version:
	def __init__(self, major:int, minor:int, code:int, build:int, buildType:int):
		self.major=major
		self.minor=minor
		self.code=code
		self.build=build
		self.buildType=buildType