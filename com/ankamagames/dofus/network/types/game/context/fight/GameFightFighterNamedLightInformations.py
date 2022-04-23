from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations


class GameFightFighterNamedLightInformations(GameFightFighterLightInformations):
    name:str
    

    def init(self, name_:str, id_:int, wave_:int, level_:int, breed_:int, sex_:bool, alive_:bool):
        self.name = name_
        
        super().__init__(id_, wave_, level_, breed_, sex_, alive_)
    
    