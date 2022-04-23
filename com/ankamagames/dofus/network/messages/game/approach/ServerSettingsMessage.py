from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ServerSettingsMessage(NetworkMessage):
    lang:str
    community:int
    gameType:int
    arenaLeaveBanTime:int
    itemMaxLevel:int
    isMonoAccount:bool
    hasFreeAutopilot:bool
    isMonoAccount:bool
    hasFreeAutopilot:bool
    

    def init(self, lang_:str, community_:int, gameType_:int, arenaLeaveBanTime_:int, itemMaxLevel_:int, isMonoAccount_:bool, hasFreeAutopilot_:bool):
        self.lang = lang_
        self.community = community_
        self.gameType = gameType_
        self.arenaLeaveBanTime = arenaLeaveBanTime_
        self.itemMaxLevel = itemMaxLevel_
        self.isMonoAccount = isMonoAccount_
        self.hasFreeAutopilot = hasFreeAutopilot_
        
        super().__init__()
    
    