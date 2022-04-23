from com.ankamagames.dofus.network.types.game.approach.ServerSessionConstant import ServerSessionConstant


class ServerSessionConstantLong(ServerSessionConstant):
    value:int
    

    def init(self, value_:int, id_:int):
        self.value = value_
        
        super().__init__(id_)
    
    