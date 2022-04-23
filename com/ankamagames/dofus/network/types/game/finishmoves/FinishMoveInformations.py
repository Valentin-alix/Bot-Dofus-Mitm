from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class FinishMoveInformations(NetworkMessage):
    finishMoveId:int
    finishMoveState:bool
    

    def init(self, finishMoveId_:int, finishMoveState_:bool):
        self.finishMoveId = finishMoveId_
        self.finishMoveState = finishMoveState_
        
        super().__init__()
    
    