from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class Version(NetworkMessage):
    major:int
    minor:int
    code:int
    build:int
    buildType:int
    

    def init(self, major_:int, minor_:int, code_:int, build_:int, buildType_:int):
        self.major = major_
        self.minor = minor_
        self.code = code_
        self.build = build_
        self.buildType = buildType_
        
        super().__init__()
    
    