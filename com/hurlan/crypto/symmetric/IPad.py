from abc import ABC
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray


class IPad(ABC):
    def pad(self, src: ByteArray) -> None:
        pass

    def unpad(self, src: ByteArray) -> None:
        pass

    def setBlockSize(self, blockSize: int) -> None:
        pass
