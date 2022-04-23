from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MapObstacle(NetworkMessage):
    obstacleCellId:int
    state:int
    

    def init(self, obstacleCellId_:int, state_:int):
        self.obstacleCellId = obstacleCellId_
        self.state = state_
        
        super().__init__()
    
    