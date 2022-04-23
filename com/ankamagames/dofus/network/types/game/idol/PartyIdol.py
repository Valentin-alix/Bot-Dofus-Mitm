from com.ankamagames.dofus.network.types.game.idol.Idol import Idol


class PartyIdol(Idol):
    ownersIds:list[int]
    

    def init(self, ownersIds_:list[int], id_:int, xpBonusPercent_:int, dropBonusPercent_:int):
        self.ownersIds = ownersIds_
        
        super().__init__(id_, xpBonusPercent_, dropBonusPercent_)
    
    