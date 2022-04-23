from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.hurlan.crypto.symmetric.IPad import IPad


class NullPad(IPad):
    def NullPad(self):
        super().__init__()

    def unpad(self, a: ByteArray) -> None:
        pass

    def pad(self, a: ByteArray) -> None:
        pass

    def setBlockSize(self, bs: int):
        pass
