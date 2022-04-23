from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightFighterLightInformations(NetworkMessage):
    id:int
    wave:int
    level:int
    breed:int
    sex:bool
    alive:bool
    sex:bool
    alive:bool
    

    def init(self, id_:int, wave_:int, level_:int, breed_:int, sex_:bool, alive_:bool):
        self.id = id_
        self.wave = wave_
        self.level = level_
        self.breed = breed_
        self.sex = sex_
        self.alive = alive_
        
        super().__init__()
    
    