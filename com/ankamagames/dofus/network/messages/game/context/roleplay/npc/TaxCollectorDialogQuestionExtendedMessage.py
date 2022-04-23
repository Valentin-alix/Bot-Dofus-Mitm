from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.TaxCollectorDialogQuestionBasicMessage import TaxCollectorDialogQuestionBasicMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
    


class TaxCollectorDialogQuestionExtendedMessage(TaxCollectorDialogQuestionBasicMessage):
    maxPods:int
    prospecting:int
    wisdom:int
    taxCollectorsCount:int
    taxCollectorAttack:int
    kamas:int
    experience:int
    pods:int
    itemsValue:int
    

    def init(self, maxPods_:int, prospecting_:int, wisdom_:int, taxCollectorsCount_:int, taxCollectorAttack_:int, kamas_:int, experience_:int, pods_:int, itemsValue_:int, guildInfo_:'BasicGuildInformations'):
        self.maxPods = maxPods_
        self.prospecting = prospecting_
        self.wisdom = wisdom_
        self.taxCollectorsCount = taxCollectorsCount_
        self.taxCollectorAttack = taxCollectorAttack_
        self.kamas = kamas_
        self.experience = experience_
        self.pods = pods_
        self.itemsValue = itemsValue_
        
        super().__init__(guildInfo_)
    
    