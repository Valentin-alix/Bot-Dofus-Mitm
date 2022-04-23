from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectEffectDice(ObjectEffect):
    diceNum:int
    diceSide:int
    diceConst:int
    

    def init(self, diceNum_:int, diceSide_:int, diceConst_:int, actionId_:int):
        self.diceNum = diceNum_
        self.diceSide = diceSide_
        self.diceConst = diceConst_
        
        super().__init__(actionId_)
    
    