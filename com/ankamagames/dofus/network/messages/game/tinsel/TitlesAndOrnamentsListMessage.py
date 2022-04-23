from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TitlesAndOrnamentsListMessage(NetworkMessage):
    titles:list[int]
    ornaments:list[int]
    activeTitle:int
    activeOrnament:int
    

    def init(self, titles_:list[int], ornaments_:list[int], activeTitle_:int, activeOrnament_:int):
        self.titles = titles_
        self.ornaments = ornaments_
        self.activeTitle = activeTitle_
        self.activeOrnament = activeOrnament_
        
        super().__init__()
    
    