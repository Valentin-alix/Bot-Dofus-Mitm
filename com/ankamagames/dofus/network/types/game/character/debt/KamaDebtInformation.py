from com.ankamagames.dofus.network.types.game.character.debt.DebtInformation import DebtInformation


class KamaDebtInformation(DebtInformation):
    kamas:int
    

    def init(self, kamas_:int, id_:int, timestamp_:int):
        self.kamas = kamas_
        
        super().__init__(id_, timestamp_)
    
    