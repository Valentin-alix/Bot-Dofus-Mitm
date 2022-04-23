from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LeaveDialogMessage(NetworkMessage):
    dialogType:int
    

    def init(self, dialogType_:int):
        self.dialogType = dialogType_
        
        super().__init__()
    
    