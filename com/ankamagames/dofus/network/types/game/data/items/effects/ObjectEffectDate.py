from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectEffectDate(ObjectEffect):
    year:int
    month:int
    day:int
    hour:int
    minute:int
    

    def init(self, year_:int, month_:int, day_:int, hour_:int, minute_:int, actionId_:int):
        self.year = year_
        self.month = month_
        self.day = day_
        self.hour = hour_
        self.minute = minute_
        
        super().__init__(actionId_)
    
    