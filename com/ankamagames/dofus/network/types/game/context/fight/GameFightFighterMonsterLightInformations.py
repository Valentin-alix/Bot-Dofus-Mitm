from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations


class GameFightFighterMonsterLightInformations(GameFightFighterLightInformations):
    creatureGenericId:int
    

    def init(self, creatureGenericId_:int, id_:int, wave_:int, level_:int, breed_:int, sex_:bool, alive_:bool):
        self.creatureGenericId = creatureGenericId_
        
        super().__init__(id_, wave_, level_, breed_, sex_, alive_)
    
    