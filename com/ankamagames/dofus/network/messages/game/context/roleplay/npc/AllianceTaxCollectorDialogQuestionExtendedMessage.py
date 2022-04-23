from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.TaxCollectorDialogQuestionExtendedMessage import TaxCollectorDialogQuestionExtendedMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
    


class AllianceTaxCollectorDialogQuestionExtendedMessage(TaxCollectorDialogQuestionExtendedMessage):
    alliance:'BasicNamedAllianceInformations'
    

    def init(self, alliance_:'BasicNamedAllianceInformations', maxPods_:int, prospecting_:int, wisdom_:int, taxCollectorsCount_:int, taxCollectorAttack_:int, kamas_:int, experience_:int, pods_:int, itemsValue_:int, guildInfo_:'BasicGuildInformations'):
        self.alliance = alliance_
        
        super().__init__(maxPods_, prospecting_, wisdom_, taxCollectorsCount_, taxCollectorAttack_, kamas_, experience_, pods_, itemsValue_, guildInfo_)
    
    