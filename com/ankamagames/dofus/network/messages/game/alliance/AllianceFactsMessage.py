from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformations import AllianceFactSheetInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInAllianceInformations import GuildInAllianceInformations
    


class AllianceFactsMessage(NetworkMessage):
    infos:'AllianceFactSheetInformations'
    guilds:list['GuildInAllianceInformations']
    controlledSubareaIds:list[int]
    leaderCharacterId:int
    leaderCharacterName:str
    

    def init(self, infos_:'AllianceFactSheetInformations', guilds_:list['GuildInAllianceInformations'], controlledSubareaIds_:list[int], leaderCharacterId_:int, leaderCharacterName_:str):
        self.infos = infos_
        self.guilds = guilds_
        self.controlledSubareaIds = controlledSubareaIds_
        self.leaderCharacterId = leaderCharacterId_
        self.leaderCharacterName = leaderCharacterName_
        
        super().__init__()
    
    