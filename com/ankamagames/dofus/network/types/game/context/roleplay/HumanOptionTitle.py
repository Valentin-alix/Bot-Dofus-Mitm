from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption


class HumanOptionTitle(HumanOption):
    titleId:int
    titleParam:str
    

    def init(self, titleId_:int, titleParam_:str):
        self.titleId = titleId_
        self.titleParam = titleParam_
        
        super().__init__()
    
    