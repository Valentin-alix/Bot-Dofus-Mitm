from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.npc.TaxCollectorDialogQuestionBasicMessage import TaxCollectorDialogQuestionBasicMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations
class TaxCollectorDialogQuestionExtendedMessage(TaxCollectorDialogQuestionBasicMessage):
	def __init__(self, maxPods:int, prospecting:int, alliance:BasicNamedAllianceInformations, taxCollectorsCount:int, taxCollectorAttack:int, pods:int, itemsValue:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.maxPods=maxPods
		self.prospecting=prospecting
		self.alliance=alliance
		self.taxCollectorsCount=taxCollectorsCount
		self.taxCollectorAttack=taxCollectorAttack
		self.pods=pods
		self.itemsValue=itemsValue