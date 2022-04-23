from com.ankamagames.dofus.network.messages.game.dialog.LeaveDialogMessage import LeaveDialogMessage


class ExchangeLeaveMessage(LeaveDialogMessage):
    success:bool
    

    def init(self, success_:bool, dialogType_:int):
        self.success = success_
        
        super().__init__(dialogType_)
    
    