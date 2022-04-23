from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.managers.StoreDataManager import IExternalizable
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray


class Version(IExternalizable, IDataCenter):

    _major: int = 2

    _minor: int = 0

    _code: int = 0

    _build: int = 0

    _buildType: int = 4

    def __init__(self, *args):
        split: list = None
        super().__init__()
        if not args or len(args) == 0:
            self._major = self._minor = self._code = self._build = self._buildType = 0
        else:
            if not (len(args) == 2 and isinstance(args[0], str)):
                raise Exception("invalid parameters, " + str(args))
            split = args[0].split(".")
            self._major = int(split[0])
            self._minor = int(split[1])
            self._code = int(split[2])
            self._build = int(split[3])
            self._buildType = int(args[1])

    def fromServerData(
        self, major: int, minor: int, code: int, build: int, buildType: int
    ) -> "Version":
        version: Version = Version()
        version._major = major
        version._minor = minor
        version._code = code
        version._build = build
        version._buildType = buildType
        return version

    @property
    def major(self) -> int:
        return self._major

    @property
    def minor(self) -> int:
        return self._minor

    @property
    def code(self) -> int:
        return self._code

    @property
    def build(self) -> int:
        return self._build

    @build.setter
    def build(self, value: int) -> None:
        self._build = value

    @property
    def buildType(self) -> int:
        return self._buildType

    @buildType.setter
    def buildType(self, value: int) -> None:
        self._buildType = value

    def __str__(self) -> str:
        if self._buildType == 5:
            return f"{self._major}.{self._minor}.{self._code}"
        if self._buildType == 0:
            return f"{self._major}.{self._minor}.{self._code}.{self._build}"
        return (
            f"{self._major}.{self._minor}.{self._code}.{self._build}-{self._buildType}"
        )

    def toStringForAppName(self) -> str:
        version = self._major + "." + self._minor + "." + self._code + "." + self._build
        if self._buildType == 1:
            version += "-beta"
        elif self._buildType == 3:
            version += "-testing"
        elif self._buildType == 4:
            version += "-locale"
        elif self._buildType == 5:
            version += "-debug"
        elif self._buildType == 6:
            version += "-draft"
        return version

    def equals(self, otherVersion: "Version") -> bool:
        return (
            self._major == otherVersion._major
            and self._minor == otherVersion._minor
            and self._code == otherVersion._code
            and self._build == otherVersion._build
            and self._buildType == otherVersion._buildType
        )

    def writeExternal(self, output: ByteArray) -> None:
        output.writeByte(self._major)
        output.writeByte(self._minor)
        output.writeByte(self._code)
        output.writeByte(self._build)
        output.writeByte(self._buildType)

    def readExternal(self, input: ByteArray) -> None:
        self._major = input.readUnsignedByte()
        self._minor = input.readUnsignedByte()
        self._code = input.readUnsignedByte()
        self._build = input.readUnsignedByte()
        self._buildType = input.readUnsignedByte()
