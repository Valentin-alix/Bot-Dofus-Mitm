from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedMessage import ExchangeStartedMessage
if TYPE_CHECKING:
	...
class ExchangeStartedWithPodsMessage(ExchangeStartedMessage):
	def __init__(self, firstCharacterId:float, firstCharacterCurrentWeight:int, firstCharacterMaxWeight:int, secondCharacterId:float, secondCharacterCurrentWeight:int, secondCharacterMaxWeight:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.firstCharacterId=firstCharacterId
		self.firstCharacterCurrentWeight=firstCharacterCurrentWeight
		self.firstCharacterMaxWeight=firstCharacterMaxWeight
		self.secondCharacterId=secondCharacterId
		self.secondCharacterCurrentWeight=secondCharacterCurrentWeight
		self.secondCharacterMaxWeight=secondCharacterMaxWeight