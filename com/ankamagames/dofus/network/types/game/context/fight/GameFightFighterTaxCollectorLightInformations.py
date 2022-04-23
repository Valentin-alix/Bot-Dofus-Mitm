from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations


class GameFightFighterTaxCollectorLightInformations(GameFightFighterLightInformations):
    firstNameId:int
    lastNameId:int
    

    def init(self, firstNameId_:int, lastNameId_:int, id_:int, wave_:int, level_:int, breed_:int, sex_:bool, alive_:bool):
        self.firstNameId = firstNameId_
        self.lastNameId = lastNameId_
        
        super().__init__(id_, wave_, level_, breed_, sex_, alive_)
    
    