from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ConsoleCommandsListMessage(NetworkMessage):
    aliases:list[str]
    args:list[str]
    descriptions:list[str]
    

    def init(self, aliases_:list[str], args_:list[str], descriptions_:list[str]):
        self.aliases = aliases_
        self.args = args_
        self.descriptions = descriptions_
        
        super().__init__()
    
    