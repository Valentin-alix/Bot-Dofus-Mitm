from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuildSubmitApplicationMessage:
	def __init__(self, applyText:str, guildId:int, timeSpent:int, filterLanguage:str, filterAmbiance:str, filterPlaytime:str, filterInterest:str, filterMinMaxGuildLevel:str, filterRecruitmentType:str, filterMinMaxCharacterLevel:str, filterMinMaxAchievement:str, filterSearchName:str, filterLastSort:str):
		self.applyText=applyText
		self.guildId=guildId
		self.timeSpent=timeSpent
		self.filterLanguage=filterLanguage
		self.filterAmbiance=filterAmbiance
		self.filterPlaytime=filterPlaytime
		self.filterInterest=filterInterest
		self.filterMinMaxGuildLevel=filterMinMaxGuildLevel
		self.filterRecruitmentType=filterRecruitmentType
		self.filterMinMaxCharacterLevel=filterMinMaxCharacterLevel
		self.filterMinMaxAchievement=filterMinMaxAchievement
		self.filterSearchName=filterSearchName
		self.filterLastSort=filterLastSort