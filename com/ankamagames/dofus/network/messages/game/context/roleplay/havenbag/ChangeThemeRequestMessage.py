from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChangeThemeRequestMessage(NetworkMessage):
    theme:int
    

    def init(self, theme_:int):
        self.theme = theme_
        
        super().__init__()
    
    