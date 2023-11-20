from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class SocialRecruitmentInformation:
	def __init__(self, socialId:int, recruitmentType:int, recruitmentTitle:str, recruitmentText:str, selectedLanguages:list[int], selectedCriterion:list[int], minLevel:int, lastEditPlayerName:str, lastEditDate:float):
		self.socialId=socialId
		self.recruitmentType=recruitmentType
		self.recruitmentTitle=recruitmentTitle
		self.recruitmentText=recruitmentText
		self.selectedLanguages=selectedLanguages
		self.selectedCriterion=selectedCriterion
		self.minLevel=minLevel
		self.lastEditPlayerName=lastEditPlayerName
		self.lastEditDate=lastEditDate