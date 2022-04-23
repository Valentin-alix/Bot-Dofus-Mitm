from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveDetailedInformations import QuestActiveDetailedInformations
    


class FollowedQuestsMessage(NetworkMessage):
    quests:list['QuestActiveDetailedInformations']
    

    def init(self, quests_:list['QuestActiveDetailedInformations']):
        self.quests = quests_
        
        super().__init__()
    
    