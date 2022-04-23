from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameServerInformations(NetworkMessage):
    id:int
    type:int
    status:int
    completion:int
    charactersCount:int
    charactersSlots:int
    date:int
    isMonoAccount:bool
    isSelectable:bool
    isMonoAccount:bool
    isSelectable:bool
    

    def init(self, id_:int, type_:int, status_:int, completion_:int, charactersCount_:int, charactersSlots_:int, date_:int, isMonoAccount_:bool, isSelectable_:bool):
        self.id = id_
        self.type = type_
        self.status = status_
        self.completion = completion_
        self.charactersCount = charactersCount_
        self.charactersSlots = charactersSlots_
        self.date = date_
        self.isMonoAccount = isMonoAccount_
        self.isSelectable = isSelectable_
        
        super().__init__()
    
    