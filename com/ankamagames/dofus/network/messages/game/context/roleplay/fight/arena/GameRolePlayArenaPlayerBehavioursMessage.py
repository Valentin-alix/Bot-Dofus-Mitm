from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaPlayerBehavioursMessage(NetworkMessage):
    flags:list[str]
    sanctions:list[str]
    banDuration:int
    

    def init(self, flags_:list[str], sanctions_:list[str], banDuration_:int):
        self.flags = flags_
        self.sanctions = sanctions_
        self.banDuration = banDuration_
        
        super().__init__()
    
    