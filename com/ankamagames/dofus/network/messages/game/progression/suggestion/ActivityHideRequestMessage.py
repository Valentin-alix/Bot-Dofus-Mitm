from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ActivityHideRequestMessage(NetworkMessage):
    activityId:int
    

    def init(self, activityId_:int):
        self.activityId = activityId_
        
        super().__init__()
    
    