from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectEffectInteger(ObjectEffect):
    value:int
    

    def init(self, value_:int, actionId_:int):
        self.value = value_
        
        super().__init__(actionId_)
    
    