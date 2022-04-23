from com.ankamagames.dofus.network.enums.BuildTypeEnum import BuildTypeEnum


class BuildTypeParser:
    def __init__(self):
        super().__init__()

    def getTypeName(self, type: int) -> str:
        if type == BuildTypeEnum.RELEASE:
            return "Release"
        elif type == BuildTypeEnum.BETA:
            return "Beta"
        elif type == BuildTypeEnum.ALPHA:
            return "Alpha"
        elif type == BuildTypeEnum.TESTING:
            return "Testing"
        elif type == BuildTypeEnum.INTERNAL:
            return "Local"
        elif type == BuildTypeEnum.DEBUG:
            return "Debug"
        elif type == BuildTypeEnum.DRAFT:
            return "Draft"
        else:
            return "UNKNOWN"
