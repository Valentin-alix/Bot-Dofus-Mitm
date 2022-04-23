from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations


class GameFightFighterEntityLightInformation(GameFightFighterLightInformations):
    entityModelId:int
    masterId:int
    

    def init(self, entityModelId_:int, masterId_:int, id_:int, wave_:int, level_:int, breed_:int, sex_:bool, alive_:bool):
        self.entityModelId = entityModelId_
        self.masterId = masterId_
        
        super().__init__(id_, wave_, level_, breed_, sex_, alive_)
    
    