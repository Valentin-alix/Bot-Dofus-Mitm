from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LockableShowCodeDialogMessage(NetworkMessage):
    changeOrUse:bool
    codeSize:int
    

    def init(self, changeOrUse_:bool, codeSize_:int):
        self.changeOrUse = changeOrUse_
        self.codeSize = codeSize_
        
        super().__init__()
    
    