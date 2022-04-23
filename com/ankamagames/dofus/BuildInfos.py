from com.ankamagames.dofus.misc.BuildTypeParser import BuildTypeParser
from com.ankamagames.dofus.network.enums.BuildTypeEnum import BuildTypeEnum
from com.ankamagames.jerakine.types.Version import Version
import com.ankamagames.dofus.Constants as Constants


class BuildInfos:
    with open(Constants.GAME_VERSION_PATH, "r") as fp:
        VERSION: Version = Version(fp.read().strip(), BuildTypeEnum.RELEASE.value)

    BUILD_DATE: str = "01/Jan/1970"

    def __init__(self):
        super().__init__()

    @property
    def buildTypeName(self) -> str:
        return BuildTypeParser.getTypeName(self.VERSION.buildType)

    @property
    def BUILD_TYPE(self) -> int:
        return self.VERSION.buildType
