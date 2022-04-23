from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectEffectDuration(ObjectEffect):
    days:int
    hours:int
    minutes:int
    

    def init(self, days_:int, hours_:int, minutes_:int, actionId_:int):
        self.days = days_
        self.hours = hours_
        self.minutes = minutes_
        
        super().__init__(actionId_)
    
    