from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectEffectMinMax(ObjectEffect):
    min:int
    max:int
    

    def init(self, min_:int, max_:int, actionId_:int):
        self.min = min_
        self.max = max_
        
        super().__init__(actionId_)
    
    