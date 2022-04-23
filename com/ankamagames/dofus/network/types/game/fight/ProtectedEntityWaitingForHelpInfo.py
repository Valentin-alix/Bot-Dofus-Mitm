from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ProtectedEntityWaitingForHelpInfo(NetworkMessage):
    timeLeftBeforeFight:int
    waitTimeForPlacement:int
    nbPositionForDefensors:int
    

    def init(self, timeLeftBeforeFight_:int, waitTimeForPlacement_:int, nbPositionForDefensors_:int):
        self.timeLeftBeforeFight = timeLeftBeforeFight_
        self.waitTimeForPlacement = waitTimeForPlacement_
        self.nbPositionForDefensors = nbPositionForDefensors_
        
        super().__init__()
    
    