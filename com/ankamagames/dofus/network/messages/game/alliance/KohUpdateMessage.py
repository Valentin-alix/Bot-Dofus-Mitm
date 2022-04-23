from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations
    


class KohUpdateMessage(NetworkMessage):
    alliances:list['AllianceInformations']
    allianceNbMembers:list[int]
    allianceRoundWeigth:list[int]
    allianceMatchScore:list[int]
    allianceMapWinners:list['BasicAllianceInformations']
    allianceMapWinnerScore:int
    allianceMapMyAllianceScore:int
    nextTickTime:int
    

    def init(self, alliances_:list['AllianceInformations'], allianceNbMembers_:list[int], allianceRoundWeigth_:list[int], allianceMatchScore_:list[int], allianceMapWinners_:list['BasicAllianceInformations'], allianceMapWinnerScore_:int, allianceMapMyAllianceScore_:int, nextTickTime_:int):
        self.alliances = alliances_
        self.allianceNbMembers = allianceNbMembers_
        self.allianceRoundWeigth = allianceRoundWeigth_
        self.allianceMatchScore = allianceMatchScore_
        self.allianceMapWinners = allianceMapWinners_
        self.allianceMapWinnerScore = allianceMapWinnerScore_
        self.allianceMapMyAllianceScore = allianceMapMyAllianceScore_
        self.nextTickTime = nextTickTime_
        
        super().__init__()
    
    