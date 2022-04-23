from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations
    


class QuestListMessage(NetworkMessage):
    finishedQuestsIds:list[int]
    finishedQuestsCounts:list[int]
    activeQuests:list['QuestActiveInformations']
    reinitDoneQuestsIds:list[int]
    

    def init(self, finishedQuestsIds_:list[int], finishedQuestsCounts_:list[int], activeQuests_:list['QuestActiveInformations'], reinitDoneQuestsIds_:list[int]):
        self.finishedQuestsIds = finishedQuestsIds_
        self.finishedQuestsCounts = finishedQuestsCounts_
        self.activeQuests = activeQuests_
        self.reinitDoneQuestsIds = reinitDoneQuestsIds_
        
        super().__init__()
    
    