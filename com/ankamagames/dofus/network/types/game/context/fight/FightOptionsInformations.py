from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class FightOptionsInformations(NetworkMessage):
    isSecret:bool
    isRestrictedToPartyOnly:bool
    isClosed:bool
    isAskingForHelp:bool
    isSecret:bool
    isRestrictedToPartyOnly:bool
    isClosed:bool
    isAskingForHelp:bool
    

    def init(self, isSecret_:bool, isRestrictedToPartyOnly_:bool, isClosed_:bool, isAskingForHelp_:bool):
        self.isSecret = isSecret_
        self.isRestrictedToPartyOnly = isRestrictedToPartyOnly_
        self.isClosed = isClosed_
        self.isAskingForHelp = isAskingForHelp_
        
        super().__init__()
    
    