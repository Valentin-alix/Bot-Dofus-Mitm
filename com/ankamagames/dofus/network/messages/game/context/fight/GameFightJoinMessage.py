from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightJoinMessage(NetworkMessage):
    timeMaxBeforeFightStart:int
    fightType:int
    isTeamPhase:bool
    canBeCancelled:bool
    canSayReady:bool
    isFightStarted:bool
    isTeamPhase:bool
    canBeCancelled:bool
    canSayReady:bool
    isFightStarted:bool
    

    def init(self, timeMaxBeforeFightStart_:int, fightType_:int, isTeamPhase_:bool, canBeCancelled_:bool, canSayReady_:bool, isFightStarted_:bool):
        self.timeMaxBeforeFightStart = timeMaxBeforeFightStart_
        self.fightType = fightType_
        self.isTeamPhase = isTeamPhase_
        self.canBeCancelled = canBeCancelled_
        self.canSayReady = canSayReady_
        self.isFightStarted = isFightStarted_
        
        super().__init__()
    
    